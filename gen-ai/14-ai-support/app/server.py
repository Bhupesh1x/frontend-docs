import os

from uuid import uuid4
from fastapi import FastAPI, UploadFile, HTTPException, File

from .lib.file import save_to_desk
from .lib.utils import getPdfChunks

app = FastAPI(title="ai-support")

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
  
  print("🤖", chunks)
  
  return {"status": "File saved"}