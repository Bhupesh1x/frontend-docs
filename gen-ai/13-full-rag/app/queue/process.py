
import os

from rq import Queue
from redis import Redis

from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
host = os.getenv("host")
port = os.getenv("port")
username = os.getenv("username")
password = os.getenv("password")


q = Queue(connection=Redis(
    host=host,
    port=port,
    decode_responses=True,
    username=username,
    password=password
  ))


