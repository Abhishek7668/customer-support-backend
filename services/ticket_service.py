from models.ticket import create_ticket_document

from repositry.ticket_repo import TicketRepository


class TicketService:

    @staticmethod
    async def create(

        user_id,

        session_id,

        question,

        priority,

        assigned_agent="Support Team"

    ):

        ticket = create_ticket_document(

            user_id=user_id,

            session_id=session_id,

            question=question,

            priority=priority,

            assigned_agent=assigned_agent

        )

        await TicketRepository.create(ticket)

        return ticket

    @staticmethod
    async def get_all():

        return await TicketRepository.get_all()

    @staticmethod
    async def get_ticket(

        ticket_number

    ):

        return await TicketRepository.get_by_ticket_number(

            ticket_number

        )

    @staticmethod
    async def update_ticket_status(

        ticket_number,

        status

    ):

        return await TicketRepository.update_status(

            ticket_number,

            status

        )