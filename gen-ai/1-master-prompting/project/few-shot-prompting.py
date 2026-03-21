import os

from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenRouter(
    api_key=api_key
)

system_prompt = """
You are an AI Assistant who is specialized in maths.
You should not answer any query, that is not related to the maths.

Example:
Input: 2 + 2
Output: 2 + 2 is 4 which is calculated by adding 2 with 2.

Example:
Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by multiplying 3 with 10. Fun fact: You can even multiply the 10 with 3 and get the same result.

Example: 
Input: What is the color of sky?
Output: Bruh? You serious? That's not maths.
"""


response = client.chat.send(
    model="openrouter/free",
    messages=[
        {"role": "system", "content": system_prompt },
        {"role": "user", "content": "What is the name of the us president?"}
    ]
)

print(response.choices[0].message.content)