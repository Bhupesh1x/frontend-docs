from tinydb import TinyDB, Query

# Initialize DB
db = TinyDB("db.json")
files_table = db.table("files")
File = Query()