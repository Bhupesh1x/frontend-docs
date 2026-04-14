import os

from dotenv import load_dotenv
from typing import Literal
from pydantic import BaseModel
from typing_extensions import TypedDict

from openai import OpenAI
from langsmith.wrappers import wrap_openai
from langgraph.graph import StateGraph, START, END

load_dotenv()

api_key = os.getenv("AI_API_KEY")

# Schema
class DetectQueryResponse(BaseModel):
  is_coding_question: bool
  
class UserQueryResponse(BaseModel):
  ai_response: str

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

class State(TypedDict):
  user_message: str
  ai_message: str
  is_coding_question: bool


def detect_query(state: State):
  user_message = state.get("user_message")
  
  # Ai call
  SYSTEM_PROMPT = """
    You are an AI Assistant. Your job is to detect if the user question is related to coding or not.
    Please return the response in specified JSON boolean only
  """
  
  
  result = client.chat.completions.parse(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    # model="llama-3.3-70b-versatile",
    messages=[
      { "role": "system", "content": SYSTEM_PROMPT },
      { "role": "user", "content": user_message }
    ],
    response_format=DetectQueryResponse
  )
  
  print("👤 User question ->", user_message)
  print("🤖 Ai Identification ->" , result.choices[0].message.parsed)
  
  state["is_coding_question"] = result.choices[0].message.parsed.is_coding_question
  return state
  
def solve_coding_question(state: State):
  user_message = state.get("user_message")
  
  # Ai call
  SYSTEM_PROMPT = """
    You are an helpful AI Coding Assistant. Your Job is to solve the user query based on coding problem user is facing.
    Please return the response in specified JSON format only
  """
  
  
  result = client.chat.completions.parse(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      { "role": "system", "content": SYSTEM_PROMPT },
      { "role": "user", "content": user_message }
    ],
    response_format=UserQueryResponse
  )
  
  state["ai_message"] = result.choices[0].message.parsed.ai_response
  
  return state

def solve_normal_question(state: State):
  user_message = state.get("user_message")
   
  # Ai Call
  SYSTEM_PROMPT = """
    You are an helpful AI Assistant. Your Job is to chat with user
    Please return the response in specified JSON format only
  """
  
  result = client.chat.completions.parse(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      { "role": "system", "content": SYSTEM_PROMPT },
      { "role": "user", "content": user_message }
    ],
    response_format=UserQueryResponse
  )
  
  state["ai_message"] = result.choices[0].message.parsed.ai_response
  
  return state

def route_edge(state: State) -> Literal["solve_coding_question", "solve_normal_question"]:
  is_coding_question = state.get("is_coding_question")
  
  if is_coding_question:
    return "solve_coding_question"
  else:
    return "solve_normal_question"
  

graph_builder = StateGraph(State)

graph_builder.add_node("detect_query", detect_query)
graph_builder.add_node("solve_coding_question", solve_coding_question)
graph_builder.add_node("solve_normal_question", solve_normal_question)
  
graph_builder.add_edge(START, "detect_query")   
graph_builder.add_conditional_edges("detect_query", route_edge)
   
graph_builder.add_edge("solve_coding_question", END)   
graph_builder.add_edge("solve_normal_question", END)

graph = graph_builder.compile()


def call_graph():
  state = {
    # "user_message": "Hey there! How are you!",
    "user_message": "What is pydantic in python?",
    "ai_message": "",
    "is_coding_question": False
  }
  
  result = graph.invoke(state)
  
  print("Final result", result)
  
  
call_graph()  
   