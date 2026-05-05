from fastapi import FastAPI

app = FastAPI(title="ai-support")

@app.get("/")
def status():
  return {"status": "Health OK!"}