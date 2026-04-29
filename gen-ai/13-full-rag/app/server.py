from uuid import uuid4

from fastapi import FastAPI, UploadFile

from .utils.file import save_to_desk

app = FastAPI(title="full-rag")

@app.get("/")
def status():
  return {"status": "Health OK!"}

@app.post("/upload")
async def upload_file(file: UploadFile):
  
  id = uuid4()
  
  file_path = f"./mnt/uploads/{id}/{file.filename}"
  
  await save_to_desk(file=await file.read(), path=file_path)
  
  return { "file_id": id }