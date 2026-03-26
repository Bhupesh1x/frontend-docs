import os
import json
import requests
import platform

from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

def get_weather(city: str):
    print("Tool called: get_weather", city)
    
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    
    return f"Failed to fetch the weather of {city}. Please check after sometime"

def get_os():
    os_name = platform.system()
    return os_name

def execute_command(command: str):
    result = os.system(command=command)
    
    return result

available_tools = {
    "get_weather": get_weather,
    "execute_command": execute_command,
    "get_os": get_os,
}

system_prompt = """
You are an helpful AI Assistant. Who is specialized in resolving user query.
You work on start, plan, action, observation, output mode.
For the given user query and available tools, Plan the step by step execution based on the planing.

Based on the user query pick the relevant tool from the available tool. And based on the tool selection you perform an action to call the tool.
Wait for the observation and based on the observation from the tool call resolve the user query.

Rules:
1. Follow the strict JSON output as Output schema.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query

Output JSON Format:
{{ "step": "string", "content": "string", "function": "The name of function it step is action", "input": "The input parameter for the function" }}

Available Tools:

- get_weather: Takes the city as the input parameter and returns the current weather of the city and if failed to fetch the weather for some reason we get the appropriate message like - "Failed to fetch the weather of city. Please check after sometime.
- get_os: Takes no parameter just returns user os information
- execute_command: Takes the command as the input and execute it on the system and return the result. We can check the os info of the user using get_os tool first before executing the commands. If the return value from the function is 0 then the command executed successfully otherwise it's not and we got an issue which we can show 

Example:
Input: What is the weather of mumbai?
Output: {{ "step": "plan", "content": "The user is interested in weather data for mumbai" }}
Output: {{ "step": "plan", "content": "From the available tool i should call the get_weather" }}
Output: {{ "step": "action", "function": "get_weather", "input": "mumbai" }}
Output: {{ "step": "observation", "content": "32 degree cel" }}
Output: {{ "step": "output", "content": "The weather of mumbai is 32 degree cel. Which is quite hot right now!" }}

Input: Can you please create a file called magic.txt in the current directory?
Output: {{ "step": "plan", "content": "The user is interested in creating a file called magic.txt" }}
Output: {{ "step": "plan", "content": "From the available tool first i should call the get_os to get the user os info" }}
Output: {{ "step": "action", "function": "get_os", "input": "" }}
Output: {{ "step": "observation", "content": "Windows" }}
Output: {{ "step": "plan", "content": "The user has the Windows system so i can use the windows commands with execute_command tool" }}
Output: {{ "step": "action", "function": "execute_command", "input": "type nul > magic.txt" }}
Output: {{ "step": "observation", "content": "0"  }}
Output: {{ "step": "output", "content": "The file magic.txt is successfully created in the current directory" }}
"""

print(execute_command("touch magic.txt"))
client = OpenRouter(
    api_key=api_key
)

response = client.chat.send(
    model="openrouter/free",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Can you please create a file called magic.txt in the current directory in my windows system?"},
        
        # 
        {"role": "assistant", "content": json.dumps({"step": "plan", "content": "User wants to create a file called magic.txt in the current directory on Windows. I need to first check the OS to confirm it's Windows, then create the file using appropriate command."})},
        {"role": "assistant", "content": json.dumps({"step": "action", "function": "get_os", "input": ""})},
        {"role": "assistant", "content": json.dumps({"step": "observation", "content": "Windows" })},
        {"role": "assistant", "content": json.dumps({"step": "plan", "content": "The OS is Windows. Now I'll create the file using the 'type' command with nul to create an empty file called magic.txt using execute_command tool."})},
        {"role": "assistant", "content": json.dumps({"step": "action", "function": "execute_command", "input": "type nul > magic.txt"})},
        {"role": "assistant", "content": json.dumps({"step": "observation", "content": "0"})},
        {"role": "assistant", "content": json.dumps({"step": "output", "content": "The file magic.txt is created successfully in the current directory"})},
    ],
    response_format={"type": "json_object"}
)

msg = response.choices[0].message

raw_content = msg.content or msg.reasoning

print(raw_content)