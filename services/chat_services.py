from agents.intent_detector import IntentDetector
from agents.router import AgentRouter
from agents.response_aggregator import ResponseAggregator
from agents.escalation import EscalationEngine

from services.ticket_service import TicketService
from services.conversation_service import ConversationService
from services.session_service import SessionService

from rag.pipline import RAGPipeline

import time


class ChatService:

    @staticmethod
    async def chat(

        user_id: str,
        session_id: str,
        question: str,

    ):

        # -----------------------------------
        # Response Timer Start
        # -----------------------------------

        start_time = time.perf_counter()

        # -----------------------------------
        # Session Update
        # -----------------------------------

        await SessionService.update_session(

            user_id=user_id,
            session_id=session_id,
            question=question

        )

        # -----------------------------------
        # Intent Detection
        # -----------------------------------

        intents = IntentDetector.detect_multiple(question)

        # -----------------------------------
        # Agent Routing
        # -----------------------------------

        agent_responses = AgentRouter.route_multiple(question)

        # -----------------------------------
        # Aggregate Agent Context
        # -----------------------------------

        agent_context = ResponseAggregator.aggregate(

            agent_responses

        )

        # -----------------------------------
        # Conversation History
        # -----------------------------------

        history = await ConversationService.get_recent_history(

            user_id,
            session_id

        )

        # -----------------------------------
        # Escalation
        # -----------------------------------

        escalation = EscalationEngine.analyze(question)

        # -----------------------------------
        # Automatic Ticket Creation
        # -----------------------------------

        ticket = None

        if escalation["escalate"]:

            ticket = await TicketService.create(

                user_id=user_id,

                session_id=session_id,

                question=question,

                priority=escalation["priority"],

                assigned_agent="Support Team"

            )

            print("=" * 60)
            print("Ticket Created :", ticket["ticket_number"])
            print("=" * 60)

        # -----------------------------------
        # RAG + Gemini
        # -----------------------------------

        answer = RAGPipeline.ask(

            question,

            history,

            agent_context

        )

        # -----------------------------------
        # Response Timer End
        # -----------------------------------

        end_time = time.perf_counter()

        response_time = round(

            end_time - start_time,

            2

        )

        # -----------------------------------
        # Save Conversation
        # -----------------------------------

        await ConversationService.save(

            user_id=user_id,

            session_id=session_id,

            question=question,

            answer=answer,

            intent=",".join(

                [

                    intent.value

                    for intent in intents

                ]

            ),

            agent=", ".join(

                [

                    response["agent"]

                    for response in agent_responses

                ]

            ),

            priority=escalation["priority"],

            escalate=escalation["escalate"],

            response_time=response_time

        )

        # -----------------------------------
        # API Response
        # -----------------------------------

        return {

            "intent": [

                intent.value

                for intent in intents

            ],

            "agent": [

                response["agent"]

                for response in agent_responses

            ],

            "answer": answer,

            "priority": escalation["priority"],

            "escalate": escalation["escalate"],

            "ticket_number": (

                ticket["ticket_number"]

                if ticket

                else None

            ),

            "response_time": f"{response_time} sec"

        }