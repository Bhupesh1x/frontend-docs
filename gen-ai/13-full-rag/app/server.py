from fastapi import FastAPI

app = FastAPI(title="full-rag")

@app.get("/")
def status():
  return {"status": "Health OK!"}