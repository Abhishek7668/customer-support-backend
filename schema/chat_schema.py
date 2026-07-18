from pydantic import BaseModel


class ChatRequest(BaseModel):

    session_id: str

    question: str


class ChatResponse(BaseModel):

    success: bool

    answer: str

    agent: str

    intent: str