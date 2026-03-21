import os

from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenRouter(
    api_key=api_key
)

response = client.chat.send(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": "What is 2 + 2?"}
    ]
)

print(response.choices[0].message.content)