from agents.intent_detector import IntentDetector, Intent

from agents.biling_agent import BillingAgent
from agents.technical_agent import TechnicalAgent
from agents.product_agent import ProductAgent
from agents.complaint_agent import ComplaintAgent
from agents.faq_agent import FAQAgent


class AgentRouter:

    @staticmethod
    def route(query: str):

        intent = IntentDetector.detect(query)

        if intent == Intent.BILLING:
            return BillingAgent.handle(query)

        elif intent == Intent.TECHNICAL:
            return TechnicalAgent.handle(query)

        elif intent == Intent.PRODUCT:
            return ProductAgent.handle(query)

        elif intent == Intent.COMPLAINT:
            return ComplaintAgent.handle(query)

        elif intent == Intent.FAQ:
            return FAQAgent.handle(query)

        return {

            "agent": "Unknown",

            "response": "Sorry, I could not understand your request."
        }