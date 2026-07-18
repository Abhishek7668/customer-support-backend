from fastapi import APIRouter

from services.ticket_service import TicketService

from schema.ticket import UpdateTicketStatus

router = APIRouter(

    prefix="/tickets",

    tags=["Tickets"]

)


@router.get("")

async def get_all_tickets():

    tickets = await TicketService.get_all()

    return {

        "success": True,

        "tickets": tickets

    }


@router.get("/{ticket_number}")

async def get_ticket(

    ticket_number: str

):

    ticket = await TicketService.get_ticket(

        ticket_number

    )

    return {

        "success": True,

        "ticket": ticket

    }


@router.put("/{ticket_number}")

async def update_ticket(

    ticket_number: str,

    request: UpdateTicketStatus

):

    ticket = await TicketService.update_ticket_status(

        ticket_number,

        request.status

    )

    return {

        "success": True,

        "ticket": ticket

    }