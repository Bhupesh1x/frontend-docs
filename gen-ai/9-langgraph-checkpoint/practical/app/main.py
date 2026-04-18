import os

from dotenv import load_dotenv
from langgraph.checkpoint.redis import RedisSaver

from .graph import create_chat_graph

load_dotenv()

redis_url = os.getenv("REDIS_URL")

config = {"configurable": {"thread_id": "2"}}

def init():
  
  with RedisSaver.from_conn_string(redis_url) as checkpointer:
    checkpointer.setup()
    graph_with_redis = create_chat_graph(checkpointer)
    
    while True:
      user_input = input("Your query: ")
      
      for event in graph_with_redis.stream({"messages": [{"role": "user", "content": user_input}]}, stream_mode='values', config = config):
        if "messages" in event:
          event["messages"][-1].pretty_print()
    
    
init()