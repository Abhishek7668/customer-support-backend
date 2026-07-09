from core.database import  get_database

class UserRepository:

    @staticmethod
    async def get_by_email(email: str):
        db = get_database()
        return await db.users.find_one({"email": email.lower()})

    @staticmethod
    async def create(user_data: dict):
        db = get_database()

        result = await db.users.insert_one(user_data)

        return result.inserted_id