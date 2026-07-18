from models.conversetion import create_conversation_document
from repositry.conversetion_repo import ConversationRepository


class ConversationService:

    @staticmethod
    async def save(

        user_id,

        session_id,

        question,

        answer,

        intent,

        agent,

        priority,

        escalate,

        response_time

    ):

        document = create_conversation_document(

            user_id,

            session_id,

            question,

            answer,

            intent,

            agent,

            priority,

            escalate,

            response_time

        )

        return await ConversationRepository.save(document)


    @staticmethod
    async def history(

        user_id,

        session_id

    ):

        return await ConversationRepository.get_history(

            user_id,

            session_id

        )


    @staticmethod
    async def get_recent_history(

        user_id,

        session_id,

        limit=5

    ):

        history = await ConversationRepository.get_history(

            user_id,

            session_id

        )

        return history[-limit:]