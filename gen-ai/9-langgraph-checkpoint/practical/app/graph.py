import os

from typing import Annotated
from dotenv import load_dotenv
from typing_extensions import TypedDict

from langchain_core.messages import SystemMessage
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END


load_dotenv()

class State(TypedDict):
  messages: Annotated[list, add_messages]
 
# llm = init_chat_model(model_provider='groq', model='meta-llama/llama-4-scout-17b-16e-instruct')  
llm = init_chat_model(model_provider='groq', model='llama-3.3-70b-versatile')  
 
def chatbot(state: State):
  messages = state.get("messages")
  
  system_msg = SystemMessage(
    content=(
        "You are a helpful assistant.\n"
        "If the user has shared information (like names, relationships), "
        "you MUST use that information to answer future questions.\n"
        "Never say you don't have memory if the information exists in the chat history."
    )
  )
  
  response = llm.invoke([system_msg] + messages)
  
  # The state will append the new messages in the array
  return {"messages": [response]}
   
   
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def create_chat_graph(checkpointer):
  return graph_builder.compile(checkpointer=checkpointer)
   