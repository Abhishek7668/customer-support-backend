import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings


async def main():

    client = AsyncIOMotorClient(settings.MONGO_URI)

    db = client[settings.DB_NAME]

    collection = db["health_check"]

    result = await collection.insert_one({
        "status": "OK"
    })

    print("Inserted ID:", result.inserted_id)

    document = await collection.find_one({
        "_id": result.inserted_id
    })

    print(document)

    client.close()


asyncio.run(main())