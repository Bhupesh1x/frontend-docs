from fastapi import FastAPI, UploadFile, HTTPException, Form, File

from .db.db import files_table
from .utils.constants import STATUS
from .utils.file import save_to_desk

from .queue.process import q
from app.queue.worker import process_file

app = FastAPI(title="full-rag")

@app.get("/")
def status():
  return {"status": "Health OK!"}

@app.get("/{id}")
async def get_file_by_id(id: str):
  file = files_table.get(doc_id=id)
  
  if not file:
    raise HTTPException(status_code=404, detail="Item not found")
  
  return file

@app.post("/upload")
async def upload_file(job_description: str = Form(...), file: UploadFile = File(...)):  
  
  if not file:
    raise HTTPException(status_code=400, detail="File is required")
  
  if not job_description.strip():
    raise HTTPException(status_code=400, detail="Job description is required")
  
  file_info = {
    "name": file.filename,
    "status": STATUS["SAVING"]
  }
  
  # Insert the file info in db
  file_id = files_table.insert(file_info)
  
  file_path = f"./mnt/uploads/{file_id}/{file.filename}"
  
  # Save file to disk
  await save_to_desk(file=await file.read(), path=file_path)
  
  q.enqueue(process_file, file_id, file_path, job_description)
  
  # Update file status to queued
  files_table.update(
    {"status": STATUS["QUEUED"]},
    doc_ids=[file_id]
  )
  
  return { "file_id": file_id }