from fastapi import FastAPI, UploadFile

from .db.db import files_table
from .utils.constants import STATUS
from .utils.file import save_to_desk

from .queue.process import q
from app.queue.worker import process_file

app = FastAPI(title="full-rag")

@app.get("/")
def status():
  return {"status": "Health OK!"}

@app.post("/upload")
async def upload_file(file: UploadFile):  
  file_info = {
    "name": file.filename,
    "status": STATUS["SAVING"]
  }
  
  # Insert the file info in db
  file_id = files_table.insert(file_info)
  
  file_path = f"./mnt/uploads/{file_id}/{file.filename}"
  
  # Save file to disk
  await save_to_desk(file=await file.read(), path=file_path)
  
  result = q.enqueue(process_file, file_id, file.filename)
  
  # Update file status to queued
  files_table.update(
    {"status": STATUS["QUEUED"]},
    doc_ids=[file_id]
  )
  
  return { "file_id": file_id }