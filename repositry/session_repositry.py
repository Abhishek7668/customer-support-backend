from core.database import get_database


class SessionRepository:

    @staticmethod
    async def get(

        user_id,

        session_id

    ):

        db = get_database()

        return await db.sessions.find_one({

            "user_id": user_id,

            "session_id": session_id

        })


    @staticmethod
    async def create(document):

        db = get_database()

        await db.sessions.insert_one(document)


    @staticmethod
    async def update(session):

        db = get_database()

        await db.sessions.update_one(

            {

                "_id": session["_id"]

            },

            {

                "$set": {

                    "last_message_at": session["last_message_at"],

                    "total_messages": session["total_messages"],

                    "title": session["title"]

                }

            }

        )