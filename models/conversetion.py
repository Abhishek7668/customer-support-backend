from datetime import datetime


def create_conversation_document(

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

    return {

        "user_id": user_id,

        "session_id": session_id,

        "question": question,

        "answer": answer,

        "intent": intent,

        "agent": agent,

        "priority": priority,

        "escalate": escalate,

        "response_time": response_time,

        "created_at": datetime.utcnow()

    }