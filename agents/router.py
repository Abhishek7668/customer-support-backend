from agents.intent_detector import IntentDetector, Intent

from agents.biling_agent import BillingAgent
from agents.technical_agent import TechnicalAgent
from agents.product_agent import ProductAgent
from agents.complaint_agent import ComplaintAgent
from agents.faq_agent import FAQAgent


class AgentRouter:

    @staticmethod
    def route(query: str):

        """
        Backward compatible
        Returns only first matched agent
        """

        responses = AgentRouter.route_multiple(query)

        if len(responses) == 0:

            return {

                "agent": "Unknown",

                "response": "Sorry, I could not understand your request."

            }

        return responses[0]


    @staticmethod
    def route_multiple(query: str):

        intents = IntentDetector.detect_multiple(query)

        responses = []

        for intent in intents:

            if intent == Intent.BILLING:

                responses.append(

                    BillingAgent.handle(query)

                )

            elif intent == Intent.TECHNICAL:

                responses.append(

                    TechnicalAgent.handle(query)

                )

            elif intent == Intent.PRODUCT:

                responses.append(

                    ProductAgent.handle(query)

                )

            elif intent == Intent.COMPLAINT:

                responses.append(

                    ComplaintAgent.handle(query)

                )

            elif intent == Intent.FAQ:

                responses.append(

                    FAQAgent.handle(query)

                )

        return responses