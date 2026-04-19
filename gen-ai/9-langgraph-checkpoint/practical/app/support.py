import os
import json

from dotenv import load_dotenv
from langgraph.types import Command
from langgraph.checkpoint.redis import RedisSaver

from .graph import create_chat_graph

load_dotenv()

redis_url = os.getenv("REDIS_URL")

config = {"configurable": {"thread_id": "6"}}

def init():
  
  with RedisSaver.from_conn_string(redis_url) as checkpointer:
    checkpointer.setup()
    graph_with_redis = create_chat_graph(checkpointer)
    
    state = graph_with_redis.get_state(config=config)
      
    last_message = state.values["messages"][-1]
    
    tool_calls = last_message.additional_kwargs.get("tool_calls", [])
    
    for call in tool_calls:
      if call.get("function", {}).get("name") == "human_assistance_tool":
        args = call["function"].get("arguments", "{}")
        
        try:
          args_dict = json.loads(args)
          user_query = args_dict.get("query")
        except json.JSONDecodeError:
          print("Failed to decode function arguments.")  
    
        print("User is trying to ask:", user_query)
        ans = input("Your resolution: ")
        
        resume_command = Command(resume={"data": ans})
        for event in graph_with_redis.stream(resume_command,config=config,stream_mode="values"):
          if "messages" in event:
              event["messages"][-1].pretty_print()
    
init()