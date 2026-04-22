import os

from dotenv import load_dotenv

from langgraph.types import Command
from langgraph.checkpoint.redis import RedisSaver

from .graph import create_chat_graph

load_dotenv()

redis_url = os.getenv("REDIS_URL")

config = {"configurable": {"thread_id": "10"}}

def init():
  
  with RedisSaver.from_conn_string(redis_url) as checkpointer:
    checkpointer.setup()
    graph_with_redis = create_chat_graph(checkpointer)
    
    while True:
      user_input = input("Your query: ")
      
      if user_input.lower() in {"exit", "quit", "q"}:
        print("Goodbye!")
        break
      
      for event in graph_with_redis.stream({"messages": [{"role": "user", "content": user_input}]}, stream_mode='values', config = config):
        if "messages" in event:
          event["messages"][-1].pretty_print()

      # After stream ends, check if graph is waiting on an interrupt
      state = graph_with_redis.get_state(config=config)
      pending = state.tasks[0].interrupts if state.tasks else []
      
      if pending:
        interrupt_message = pending[0].value
        print(interrupt_message, end="")
        ans = input()  
        
        for event in graph_with_redis.stream(Command(resume=ans), config=config, stream_mode="values"):
          if "messages" in event:
              event["messages"][-1].pretty_print()    
    
init()

