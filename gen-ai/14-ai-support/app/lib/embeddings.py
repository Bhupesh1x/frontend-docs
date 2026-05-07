import os
from dotenv import load_dotenv

from google import genai
from langchain.embeddings.base import Embeddings

load_dotenv(dotenv_path=".env")

GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

def embed_text(text: str):
    response = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values
  
class GeminiEmbeddings(Embeddings):
  def embed_documents(self, texts):
      response = gemini_client.models.embed_content(
          model="gemini-embedding-001",
          contents=texts
      )
      return [e.values for e in response.embeddings]

  def embed_query(self, text):
      return embed_text(text)