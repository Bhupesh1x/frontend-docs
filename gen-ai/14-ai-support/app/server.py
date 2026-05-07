import os

from uuid import uuid4
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, HTTPException, File

from .lib.file import save_to_desk
from .lib.utils import getPdfChunks
from .lib.agent import getAgent, llm
from .lib.qdrant import createVectorStore
from .constants import SEARCH_INTERPRETER_PROMPT

load_dotenv(dotenv_path=".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

QUERY_LIMIT = 3

class QueryRequest(BaseModel):
  query: str
  

app = FastAPI(title="ai-support")

@app.get("/")
def status():
  return {"status": "Health OK!"}

@app.post('/ask')
def ask(payload: QueryRequest):
  
  if not payload.query:
    raise HTTPException(status_code=400, detail="Question is required")
  
  try:
    # =================================================
    # STEP 1 → AGENT DECIDES TOOL USAGE
    # =================================================
    agent_executer = getAgent()
    agent_response = agent_executer.invoke({
      "input": payload.query,
    })
    
    # =================================================
    # STEP 2 → EXTRACT SEARCH TOOL RESULTS
    # =================================================
    tools_results = ""
    
    for step in agent_response.get("intermediate_steps", []): 
      action, observation = step
    
      if action.tool == "searchTool":
        tools_results = observation
      
    # =================================================
    # STEP 3 → HANDLE GREETINGS / NO TOOL CALL
    # =================================================  
    
    if not tools_results:
      return {
        "query": payload.query,
        "answer": agent_response["output"]
      }
      
    # =================================================
    # STEP 4 → GET SEARCH RESULTS FROM TOOL
    # =================================================
    search_prompt = f"""
      {SEARCH_INTERPRETER_PROMPT}
      
      USER QUESTION: {payload.query}
      
      SEARCH RESULTS: {tools_results}
      
      FINAL ANSWER:
    """
    
    final_answer = llm.invoke(
      search_prompt
    )
    
    return {
      "query": payload.query,
      "answer": final_answer.content
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
  
  vector_store = createVectorStore()
  
  vector_store.add_documents(chunks)
  
  return {"status": "File saved"}