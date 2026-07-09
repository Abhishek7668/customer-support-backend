import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymongo import MongoClient
from core.config import settings

client = MongoClient(
    settings.MONGO_URI,
    serverSelectionTimeoutMS=10000
)

try:
    print(client.admin.command("ping"))
    print("Connected")
except Exception as e:
    print(e)