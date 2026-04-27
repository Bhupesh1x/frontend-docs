import os
import json
import requests 

from datetime import datetime

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

JUDGE_MODEL = "qwen/qwen3-32b"
AGENT_MODEL = "llama-3.3-70b-versatile"

# ------------------------------------------------------------------ #
#  Tools
# ------------------------------------------------------------------ #

def add_numbers(a: float, b: float) -> dict:
    return {"result": a + b}
  
def get_weather(city: str) -> str:
    """Get current weather for a city"""
    print("Tool called: get_weather", city)

    try:
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return f"The weather in {city} is {response.text.strip()}."
        else:
            return f"Failed to fetch weather for {city}."

    except Exception as e:
        return f"Error fetching weather: {str(e)}"
      
def get_current_date_and_time() -> dict:
    now = datetime.now()
    return {
        "date": now.strftime("%d %B %Y"),
        "time": now.strftime("%I:%M %p"),
        "day":  now.strftime("%A"),
    }
    
    
# ------------------------------------------------------------------ #
#  Tool Registry
# ------------------------------------------------------------------ #

TOOLS = {
    "add_numbers":               add_numbers,
    "get_weather":               get_weather,
    "get_current_date_and_time": get_current_date_and_time,
}          

TOOLS_SCHEMA = [
  {
    "type": "function",
    "function": {
      "name": "add_numbers",
      "description": "Adds two numbers together and returns the results",
      "parameters": {
        "type": "object",
        "properties": {
          "a": {"type": "number", "description": "First number"},
          "b": {"type": "number", "description": "Second number"},
        },
        "required": ["a", "b"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the current weather for a city",
      "parameters": {
        "type": "object",
        "properties": {
          "city": {"type": "string", "description": "Name of the city"},
        },
        "required": ["city"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_current_date_and_time",
      "description": "Get the current date and time",
      "parameters": {
        "type": "object",
        "properties": {
          
        },
        "required": []
      }
    }
  },
]

# ------------------------------------------------------------------ #
#  Input Guardrail
#  Step 1 : Llama Guard checks if message is safe
#  Step 2 : We check if the message is relevant to what our agent can do
# ------------------------------------------------------------------ #

def check_input_safety(user_message: str) -> tuple[bool, str]:
  # Step 1 : Safety check via Llama Guard
  guard_response = client.chat.completions.create(
    model=JUDGE_MODEL,
    messages=[{"role": "user", "content": user_message}]
  )
  
  verdict = guard_response.choices[0].message.content.strip().lower()
  
  print(f"  [Judge Input Safety] Verdict: {verdict}")
  
  if verdict.startswith("unsafe"):
        return False, f"Message flagged as unsafe: {verdict}"
      
  # Step 2 : Relevance check, is the question something our agent can handle    
  
  SYSTEM_PROMPT = """
    You are a strict topic checker.
    Reply with only 'yes' if the user message is asking about:
    weather, adding numbers, or the current date and time. Reply with only 'no' for anything else. No explanation, just yes or no.
  """
  
  relevance_response = client.chat.completions.create(
    model=AGENT_MODEL,
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": user_message }
    ]
  )
  
  relevance = relevance_response.choices[0].message.content.strip().lower()
  print(f"  [Judge Relevance Check] Is relevant: {relevance}")
  
  if relevance != "yes":
    return False, "Sorry, I can only help with weather, adding numbers, or current date and time."
  
  return True, "ok"


# ------------------------------------------------------------------ #
#  Output Guardrail
#  Llama Guard checks the agent response before user sees it
# ------------------------------------------------------------------ #

def check_output_safety(agent_response: str) -> tuple[bool, str]:
  guard_response = client.chat.completions.create(
    model=JUDGE_MODEL,
    messages=[{"role": "user", "content": agent_response}]
  )
  
  verdict = guard_response.choices[0].message.content.strip().lower()
  print(f"  [Judge Output Safety] Verdict: {verdict}")
  
  if verdict.startswith("unsafe"):
    return False, "Agent response was flagged. Blocking it for safety."
  
  return True, "ok"

# ------------------------------------------------------------------ #
#  Generic Tool Handler
# ------------------------------------------------------------------ #

def handle_tool_call(tool_name: str, tool_args: dict) -> str:
  if tool_name not in TOOLS:
    return json.dumps({"error": f"Unknown tool: {tool_name}"})
  
  tool_args = tool_args or {}  # ✅ guard here
  
  print(f"  [Agent] Calling tool: {tool_name}({tool_args})")
  result = TOOLS[tool_name](**tool_args)
  return json.dumps(result)

# ------------------------------------------------------------------ #
#  Agent Loop
# ------------------------------------------------------------------ #

def run_agent(user_message: str) -> str:
  messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant with tools to add numbers, get weather, and get the current date and time."
    },
    {"role": "user", "content": user_message}
  ]  
  
  while True:
    response = client.chat.completions.create(
      model=AGENT_MODEL,
      messages=messages,
      tools=TOOLS_SCHEMA,
      tool_choice="auto"
  )

    response_message = response.choices[0].message
    messages.append(response_message)
    
    if not response_message.tool_calls:
      return response_message.content
    
    for tool_call in response_message.tool_calls:
      tool_name = tool_call.function.name
      tool_args = json.loads(tool_call.function.arguments)
      tool_result = handle_tool_call(tool_name, tool_args)
      messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": tool_result
      })


# ------------------------------------------------------------------ #
#  Full Pipeline : input guard -> agent -> output guard
# ------------------------------------------------------------------ #

def ask(user_message: str):
  print(f"\n{'='*55}")
  print(f"User: {user_message}")
  print(f"{'='*55}")      
  
  input_safe, input_reason = check_input_safety(user_message)
  
  if not input_safe:
    print(f"\n  [BLOCKED at Input] {input_reason}\n")
    return
  
  agent_answer = run_agent(user_message)
  print(f"\n  [Agent Raw Answer] {agent_answer}")
  
  output_safe, output_reason = check_output_safety(agent_answer)
  
  if not output_safe:
    print(f"\n  [BLOCKED at Output] {output_reason}\n")
    return
  
  print(f"\nFinal Answer: {agent_answer}\n")
  
  
  
if __name__ == "__main__":
    ask("What is 24 plus 76?")                                     # passes, uses add_numbers
    ask("What is the weather in Mumbai?")                          # passes, uses get_weather
    ask("What is today's date and time?")                          # passes, uses get_current_date_and_time
    ask("What is the weather in Delhi and also what time is it?")  # passes, uses two tools
    ask("Can you write me a poem?")                                # [BLOCKED at Input] Sorry, I can only help with weather, adding numbers, or current date and time. 
