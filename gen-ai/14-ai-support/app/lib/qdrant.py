import os

from dotenv import load_dotenv

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

from .embeddings import GeminiEmbeddings

load_dotenv(dotenv_path=".env")

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_VECTOR_NAME = os.getenv("QDRANT_VECTOR_NAME")
QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

embeddings = GeminiEmbeddings()

def createVectorStore():
    store = QdrantVectorStore(
      client=client,
      collection_name=QDRANT_COLLECTION_NAME,
      embedding=embeddings,
      vector_name=QDRANT_VECTOR_NAME
    )
    
    return store