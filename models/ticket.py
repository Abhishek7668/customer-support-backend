from datetime import datetime
import uuid


def create_ticket_document(

    user_id: str,

    session_id: str,

    question: str,

    priority: str,

    assigned_agent: str = "Support Team"

):

    ticket_number = f"TKT-{uuid.uuid4().hex[:8].upper()}"

    return {

        "ticket_number": ticket_number,

        "user_id": user_id,

        "session_id": session_id,

        "question": question,

        "priority": priority,

        "status": "OPEN",

        "assigned_agent": assigned_agent,

        "created_at": datetime.utcnow(),

        "updated_at": datetime.utcnow()

    }