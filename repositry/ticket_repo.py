from core.database import get_database


class TicketRepository:

    @staticmethod
    async def create(ticket):

        db = get_database()

        result = await db.tickets.insert_one(ticket)

        return str(result.inserted_id)

    @staticmethod
    async def get_all():

        db = get_database()

        cursor = db.tickets.find().sort("created_at", -1)

        tickets = await cursor.to_list(length=100)

        for ticket in tickets:

            ticket["_id"] = str(ticket["_id"])

            ticket["created_at"] = ticket["created_at"].isoformat()

            ticket["updated_at"] = ticket["updated_at"].isoformat()

        return tickets

    @staticmethod
    async def get_by_ticket_number(ticket_number):

        db = get_database()

        ticket = await db.tickets.find_one(

            {

                "ticket_number": ticket_number

            }

        )

        if ticket:

            ticket["_id"] = str(ticket["_id"])

            ticket["created_at"] = ticket["created_at"].isoformat()

            ticket["updated_at"] = ticket["updated_at"].isoformat()

        return ticket

    @staticmethod
    async def update_status(

        ticket_number,

        status

    ):

        db = get_database()

        await db.tickets.update_one(

            {

                "ticket_number": ticket_number

            },

            {

                "$set": {

                    "status": status

                }

            }

        )

        return await TicketRepository.get_by_ticket_number(ticket_number)