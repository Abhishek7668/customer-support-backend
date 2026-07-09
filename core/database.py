from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings


class MongoDB:

    client: AsyncIOMotorClient = None

    database = None


mongodb = MongoDB()

print("MONGO_URI:", settings.MONGO_URI)
print("DB_NAME:", settings.DB_NAME)


async def connect_to_mongo():

    try:

        mongodb.client = AsyncIOMotorClient(

            settings.MONGO_URI,

            serverSelectionTimeoutMS=5000

        )

        await mongodb.client.admin.command("ping")

        mongodb.database = mongodb.client[settings.DB_NAME]

        print("=" * 60)
        print("✅ MongoDB Atlas Connected Successfully")
        print(f"📂 Database : {settings.DB_NAME}")
        print("=" * 60)

    except Exception as e:

        print("=" * 60)
        print("❌ MongoDB Connection Failed")
        print(e)
        print("=" * 60)


async def close_mongo_connection():

    if mongodb.client:

        mongodb.client.close()

        print("🔒 MongoDB Connection Closed")
def get_database():
    return mongodb.database