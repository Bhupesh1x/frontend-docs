import os

from uuid import uuid4
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
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

QUERY_LIMIT = 3

class QueryRequest(BaseModel):
  query: str
  

app = FastAPI(title="ai-support")

embeddings = GeminiEmbeddings()

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

@app.get("/")
def status():
  return {"status": "Health OK!"}

@app.post('/ask')
def ask(payload: QueryRequest):
  
  if not payload.query:
    raise HTTPException(status_code=400, detail="Question is required")
  
  try:
    vector_store = QdrantVectorStore(
      client=client,
      collection_name=QDRANT_COLLECTION_NAME,
      embedding=embeddings,
      vector_name=QDRANT_VECTOR_NAME
    )
    
    # Semantic similarity search
    results = vector_store.similarity_search_with_score(
      query=payload.query,
      k=QUERY_LIMIT
    )
    
    docs = []
    context_parts = []
    
    for doc, score in results:
      docs.append({
          "content": doc.page_content,
          "metadata": doc.metadata,
          "score": score
    })
      
    context_parts.append(doc.page_content)
    
    # Combine all retrieved chunks
    context = "\n\n".join(context_parts)  
    
    # Prompt for Groq
    prompt = f"""
      You are helpful AI assistant.

      Answer the user's question ONLY using the provided context.

      If the answer is not present in the context,
      say: "I could not find the answer in the uploaded documents."
      
      Context: {context}
      
      Question: {payload.query}

      Answer:
    """
    ai_response = llm.invoke(prompt)
      
    return {
      "query": payload.query,
      "results": ai_response.content,
      "sources": docs
    }  
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))  
  

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