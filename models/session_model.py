from datetime import datetime


def create_session_document(

    user_id: str,

    session_id: str

):

    return {

        "user_id": user_id,

        "session_id": session_id,

        "title": "New Conversation",

        "status": "ACTIVE",

        "total_messages": 0,

        "started_at": datetime.utcnow(),

        "last_message_at": datetime.utcnow()

    }