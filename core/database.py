import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings


class MongoDB:

    client: AsyncIOMotorClient = None

    database = None


mongodb = MongoDB()

print("MONGO_URI:", settings.MONGO_URI, flush=True)
print("DB_NAME:", settings.DB_NAME, flush=True)


async def connect_to_mongo():
    """
    Connects to MongoDB with a hard timeout so a bad connection string,
    unreachable Atlas cluster, or slow SRV DNS lookup can NEVER block
    the app from starting and binding to the port. Any failure here is
    logged and swallowed on purpose - the app should still come up.
    """

    try:

        mongodb.client = AsyncIOMotorClient(
            settings.MONGO_URI,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
        )

        # asyncio.wait_for guards against the SRV DNS lookup itself
        # hanging, which serverSelectionTimeoutMS does NOT cover.
        await asyncio.wait_for(
            mongodb.client.admin.command("ping"),
            timeout=8,
        )

        mongodb.database = mongodb.client[settings.DB_NAME]

        print("=" * 60, flush=True)
        print("✅ MongoDB Atlas Connected Successfully", flush=True)
        print(f"📂 Database : {settings.DB_NAME}", flush=True)
        print("=" * 60, flush=True)

    except Exception as e:

        print("=" * 60, flush=True)
        print("❌ MongoDB Connection Failed (app will still start)", flush=True)
        print(e, flush=True)
        print("=" * 60, flush=True)


async def close_mongo_connection():

    if mongodb.client:

        mongodb.client.close()

        print("🔒 MongoDB Connection Closed")
def get_database():
    return mongodb.database