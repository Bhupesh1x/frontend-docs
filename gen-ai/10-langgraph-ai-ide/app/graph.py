import re
import os
import subprocess
from typing import Annotated
from dotenv import load_dotenv
from typing_extensions import TypedDict

from langchain_core.tools import tool 
from langgraph.prebuilt import ToolNode
from langgraph.types import interrupt
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage 
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AIMessage, ToolMessage


load_dotenv()

RISKY_PATTERNS = [
    r"\brm\b",
    r"\brmdir\b",
    r"\bdel\b",
    r"\bdelete\b",
    r"\bdrop\b",          # SQL DROP
    r"\btruncate\b",      # SQL TRUNCATE
    r"\bformat\b",
    r"\bmkfs\b",
    r"\bshred\b",
    r"\bchmod\b",
    r"\bchown\b",
    r">\s*/dev/",          # redirect to /dev/
    r"\bdd\b.*of=",        # dd write
]

class State(TypedDict):
  messages: Annotated[list, add_messages]
  
def is_risky_command(command: str) -> bool:
  command_lower = command.lower()
  return any(re.search(pattern, command_lower) for pattern in RISKY_PATTERNS)   
  
@tool()
def execute_command(command) -> str:
    """Execute a shell command and return its output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
        output = result.stdout
        if result.returncode != 0:
            output += f"\n[stderr]: {result.stderr}"
        return output or "[No output]"
    except Exception as e:
        return str(e)
  
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
  
tools = [execute_command]

llm = init_chat_model(model_provider='groq', model='llama-3.3-70b-versatile')  
llm_with_tools = llm.bind_tools(tools=tools)  

def human_confirmation(state: State):
  """
  Sits between chatbot → tools.
  For risky commands, calls interrupt() to pause and ask the user.
  For safe commands, passes straight through to ToolNode.
  """
  
  last_message = state["messages"][-1]
  
  # Collect any risky tool calls
  
  risky = []
  safe = []
  
  for tool_call in last_message.tool_calls:
    if tool_call["name"] == "execute_command":
      cmd = tool_call["args"].get("command", "")
      
      if is_risky_command(cmd):
        risky.append(tool_call)
      else:
        safe.append(tool_call)
    safe.append(cmd)    
  
  if risky:
    # Pause the graph — show the user what's about to run
    descriptions = [
            f"  • [{tc['name']}] `{tc['args'].get('command', '')}`"
            for tc in risky
    ]
    
    prompt = (
      "⚠️  The agent wants to run potentially destructive command(s):\n"
      + "\n".join(descriptions)
      + "\n\nType 'yes' to approve or anything else to cancel: "
    )
    
    # interrupt() suspends here; resumes with whatever the user typed
    decision = interrupt(prompt)
    
    if str(decision).strip().lower() != "yes":
      # Inject cancelled ToolMessages so the LLM knows what happened
      cancelled_msg = [
        ToolMessage(
          content="[Action rejected by user. Do NOT proceed with this action. Inform the user that the command was cancelled.]",
          tool_call_id=tc["id"],
        )
        for tc in risky
      ]
      
      return {"messages": cancelled_msg}
    
  # Approved (or no risky calls) — run normally
  return tool_node.invoke(state)
    

def chatbot(state: State):
  messages = state.get("messages")
  cwd = os.getcwd()
  
  system_msg = SystemMessage(
    content=(
       "You are a helpful assistant with access to shell commands.\n"
        f"The current working directory is: {cwd}\n"
        "Always use absolute paths or paths relative to the cwd above when working with files.\n"
        "If the user has shared information (like names, relationships), "
        "you MUST use that information to answer future questions.\n"
        "Never say you don't have memory if the information exists in the chat history."
    )
  )
  
  response = llm_with_tools.invoke([system_msg] + messages)
  
  return {"messages": [response]}
  
tool_node = ToolNode(tools=tools)

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", human_confirmation)


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

def create_chat_graph(checkpointer):
  return graph_builder.compile(checkpointer=checkpointer)

