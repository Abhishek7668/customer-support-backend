from datetime import datetime

from models.session_model import create_session_document

from repositry.session_repositry import SessionRepository


class SessionService:

    @staticmethod
    async def update_session(

        user_id,

        session_id,

        question

    ):

        session = await SessionRepository.get(

            user_id,

            session_id

        )

        if session is None:

            document = create_session_document(

                user_id,

                session_id

            )

            document["title"] = question[:40]

            document["total_messages"] = 1

            await SessionRepository.create(document)

            return

        session["last_message_at"] = datetime.utcnow()

        session["total_messages"] += 1

        await SessionRepository.update(session)