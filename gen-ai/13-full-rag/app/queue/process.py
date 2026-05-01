import os

from rq import Queue
from redis import Redis

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

REDIS_URL = os.getenv("REDIS_URL")

redis_conn = Redis.from_url(REDIS_URL, decode_responses=True)

q = Queue(connection=redis_conn)

