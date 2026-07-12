from enum import Enum


class Intent(str, Enum):

    BILLING = "billing"

    TECHNICAL = "technical"

    PRODUCT = "product"

    COMPLAINT = "complaint"

    FAQ = "faq"

    UNKNOWN = "unknown"


class IntentDetector:

    billing_keywords = [
        "payment",
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
        "install",
        "installation",
        "bug",
        "error",
        "crash",
        "otp"
    ]

    product_keywords = [
        "product",
        "feature",
        "pricing",
        "price",
        "availability",
        "compare"
    ]

    complaint_keywords = [
            "complaint",
    "complain",
    "poor",
    "bad",
    "angry",
    "frustrated",
    "issue",
    "dissatisfied",
    "not happy"

    ]

    faq_keywords = [
        "contact",
        "address",
        "office",
        "support",
        "company"
    ]

    @classmethod
    def detect(cls, message: str):

        message = message.lower()

        if any(word in message for word in cls.billing_keywords):
            return Intent.BILLING

        elif any(word in message for word in cls.technical_keywords):
            return Intent.TECHNICAL

        elif any(word in message for word in cls.product_keywords):
            return Intent.PRODUCT

        elif any(word in message for word in cls.complaint_keywords):
            return Intent.COMPLAINT

        elif any(word in message for word in cls.faq_keywords):
            return Intent.FAQ

        return Intent.UNKNOWN