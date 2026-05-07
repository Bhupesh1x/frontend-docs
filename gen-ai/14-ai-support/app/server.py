import os

from uuid import uuid4
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from fastapi import FastAPI, UploadFile, HTTPException, File

from .lib.file import save_to_desk
from .lib.utils import getPdfChunks
from .lib.embeddings import GeminiEmbeddings

load_dotenv(dotenv_path=".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")
QDRANT_VECTOR_NAME = os.getenv("QDRANT_VECTOR_NAME")

app = FastAPI(title="ai-support")

embeddings = GeminiEmbeddings()

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

@app.get("/")
def status():
  return {"status": "Health OK!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):  
  if not file:
    raise HTTPException(status_code=400, detail="File is required")
  
  id = uuid4()
  
  file_path = f"./mnt/uploads/{id}/{file.filename}"
  
  # Save file to disk
  await save_to_desk(file=await file.read(), path=file_path)
  
  chunks = None
  
  _, ext = os.path.splitext(file.filename)
  ext = ext.lower()

  if ext == ".txt":
      print(f"Text file received: {file.filename}, extension: {ext}")
      # TODO: call text processing function here

  elif ext == ".pdf":
      chunks = getPdfChunks(file_path)

  else:
      raise HTTPException(
          status_code=400,
          detail=f"Unsupported file type: {ext}"
      )
  
  vector_store = QdrantVectorStore(
    client=client,
    collection_name=QDRANT_COLLECTION_NAME,
    embedding=embeddings,
    vector_name=QDRANT_VECTOR_NAME
  )
  
  vector_store.add_documents(chunks)
  
  return {"status": "File saved"}