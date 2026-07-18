from enum import Enum


class Intent(Enum):

    BILLING = "billing"

    TECHNICAL = "technical"

    PRODUCT = "product"

    COMPLAINT = "complaint"

    FAQ = "faq"

    UNKNOWN = "unknown"


class IntentDetector:

    billing_keywords = [

        "payment",
        "paid",
        "invoice",
        "refund",
        "billing",
        "subscription",
        "premium",
        "plan"

    ]

    technical_keywords = [

        "login",
        "password",
        "error",
        "bug",
        "issue",
        "install",
        "locked",
        "reset"

    ]

    product_keywords = [

        "product",
        "feature",
        "pricing",
        "price",
        "compare",
        "available"

    ]

    complaint_keywords = [
        "complain",
        "complaint",
        "angry",
        "bad",
        "worst",
        "disappointed"

    ]

    faq_keywords = [

        "office",
        "location",
        "contact",
        "email",
        "phone"

    ]


    @staticmethod
    def detect(query: str):

        """
        Backward compatibility
        Returns first detected intent
        """

        intents = IntentDetector.detect_multiple(query)

        if intents:

            return intents[0]

        return Intent.UNKNOWN


    @staticmethod
    def detect_multiple(query: str):

        query = query.lower()

        intents = []

        if any(word in query for word in IntentDetector.billing_keywords):

            intents.append(Intent.BILLING)

        if any(word in query for word in IntentDetector.technical_keywords):

            intents.append(Intent.TECHNICAL)

        if any(word in query for word in IntentDetector.product_keywords):

            intents.append(Intent.PRODUCT)

        if any(word in query for word in IntentDetector.complaint_keywords):

            intents.append(Intent.COMPLAINT)

        if any(word in query for word in IntentDetector.faq_keywords):

            intents.append(Intent.FAQ)

        if not intents:

            intents.append(Intent.UNKNOWN)

        return intents