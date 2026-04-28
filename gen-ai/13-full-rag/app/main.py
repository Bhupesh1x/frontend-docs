import uvicorn

from tinydb import TinyDB, Query

from .server import app

# Initialize DB
db = TinyDB("db.json")
process_table = db.table("process")
Process = Query()


def main():
  uvicorn.run(app=app, host="0.0.0.0", port=8000)
  
  
main()  
