import os
import json

from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenRouter(
    api_key=api_key
)

system_prompt="""
You are an AI Assistant who is expert in breaking down complex problems and then resolve the user query.
 
For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you think again for several times then you give a output. You validate the output and then give the result with explanation and then finally you validate the output as well before giving the final result.

Follow this steps in sequence "analyse", "think", "output", "validate", and then finally "result". 

Rules:
1. Follow the strict JSON output as Output schema.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query

Output format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2?
Output: {{ step: "analyse", content: "Alright! User is interested in the math query and he is asking about the basic arithmetic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all the numbers" }}
"""


messages = [
    { "role": "system", "content": system_prompt},
]

q = input("Please ask your query? >")

messages.append(
    { "role": "user", "content": q},
)

while True:
    response = client.chat.send(
        # model="openrouter/free",
        model="stepfun/step-3.5-flash:free",
        messages=messages,
        response_format={"type": "json_object"}
    )
    msg = response.choices[0].message

    raw_content = msg.content or msg.reasoning
    
    parsed_response = json.loads(raw_content)
    messages.append({ "role": "assistant", "content": json.dumps(parsed_response) })
    
    if parsed_response.get("step") != "result":
        print(f"Step 🧠: {parsed_response.get("step")}")
        print(f"🧠: {parsed_response.get("content")}")
        continue
    
    print(f"🤖: {parsed_response.get("content")}")
    break
