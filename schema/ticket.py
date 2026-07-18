from pydantic import BaseModel


class UpdateTicketStatus(BaseModel):

    status: str