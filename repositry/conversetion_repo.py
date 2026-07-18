from core.database import get_database


class ConversationRepository:

    @staticmethod
    async def save(document):

        db = get_database()

        result = await db.conversations.insert_one(document)

        return str(result.inserted_id)

    @staticmethod
    async def get_history(

        user_id,

        session_id

    ):

        db = get_database()

        cursor = db.conversations.find(

            {

                "user_id": user_id,

                "session_id": session_id

            }

        ).sort("created_at", 1)

        history = await cursor.to_list(length=100)

        # ----------------------------------------
        # Convert MongoDB ObjectId & Datetime
        # ----------------------------------------

        for item in history:

            item["_id"] = str(item["_id"])

            if "created_at" in item:

                item["created_at"] = item["created_at"].isoformat()

        return history

    @staticmethod
    async def get_recent_history(

        user_id,

        session_id,

        limit=5

    ):

        db = get_database()

        cursor = db.conversations.find(

            {

                "user_id": user_id,

                "session_id": session_id

            }

        ).sort(

            "created_at",

            -1

        ).limit(limit)

        history = await cursor.to_list(length=limit)

        history.reverse()

        # ----------------------------------------
        # Convert MongoDB ObjectId & Datetime
        # ----------------------------------------

        for item in history:

            item["_id"] = str(item["_id"])

            if "created_at" in item:

                item["created_at"] = item["created_at"].isoformat()

        return history