import os

from typing import Annotated
from dotenv import load_dotenv
from typing_extensions import TypedDict

from langchain_core.messages import SystemMessage
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AIMessage, ToolMessage


load_dotenv()

class State(TypedDict):
  messages: Annotated[list, add_messages]
  
@tool()
def human_assistance_tool(query):
  """Request assistance from a human"""
  human_response = interrupt({"query": query}) # Graph will exit out after saving the state in the DB
  return human_response["data"] # Resume with the data once human provide it

def should_use_tools(state: State):
    messages = state.get("messages", [])
    if not messages:
        return "__end__"

    last_message = messages[-1]

    # If tool already responded → STOP
    if isinstance(last_message, ToolMessage):
        return "__end__"

    # Only call tool if last message is AI with tool calls
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"

    return "__end__"

tools = [human_assistance_tool]
 
# llm = init_chat_model(model_provider='groq', model='meta-llama/llama-4-scout-17b-16e-instruct')  
llm = init_chat_model(model_provider='groq', model='llama-3.3-70b-versatile')  
llm_with_tools = llm.bind_tools(tools=tools) 
def chatbot(state: State):
  messages = state.get("messages")
  
  system_msg = SystemMessage(
    content=(
        "You are a helpful assistant.\n"
        "If the user has shared information (like names, relationships), "
        "you MUST use that information to answer future questions.\n"
        "Never say you don't have memory if the information exists in the chat history."
        "If a human assistance tool has already been used and a response is provided, "
        "you MUST NOT call the tool again.\n"
        "Instead, respond to the user using the tool's response.\n"
        "Only call the tool if no prior human response exists.\n"
    )
  )
  
  response = llm_with_tools.invoke([system_msg] + messages)
  
  # The state will append the new messages in the array
  return {"messages": [response]}
   
   
tool_node = ToolNode(tools=tools) 
   
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "chatbot")

# For executing the tool call using langgraph prebuilt nodes
graph_builder.add_conditional_edges(
    "chatbot",
    should_use_tools,
    {
        "tools": "tools",
        "__end__": END,
    },
)
graph_builder.add_edge("tools", "chatbot")

# graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def create_chat_graph(checkpointer):
  return graph_builder.compile(checkpointer=checkpointer)
   