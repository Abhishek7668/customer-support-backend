class EscalationEngine:

    keyword_weights = {

        # ==========================
        # Payment & Billing
        # ==========================
        "payment deducted": 5,
        "money deducted": 5,
        "payment failed": 5,
        "transaction failed": 5,
        "refund": 4,
        "refund not received": 5,
        "charged twice": 5,
        "double payment": 5,
        "order not confirmed": 5,
        "billing issue": 4,

        # ==========================
        # Authentication
        # ==========================
        "login failed": 3,
        "unable to login": 3,
        "can't login": 3,
        "account locked": 4,
        "password reset": 2,

        # ==========================
        # Security
        # ==========================
        "fraud": 6,
        "fake": 6,
        "scam": 6,
        "hacked": 7,
        "security": 6,
        "data breach": 7,

        # ==========================
        # Website / System
        # ==========================
        "website down": 6,
        "server down": 6,
        "application down": 6,
        "critical": 6,

        # ==========================
        # Complaint
        # ==========================
        "complaint": 3,
        "manager": 4,
        "human": 3,
        "angry": 3,
        "frustrated": 3,
        "worst": 3,
        "bad service": 3,
        "poor service": 3,

        # ==========================
        # Legal
        # ==========================
        "legal": 8,
        "lawsuit": 8,
        "consumer court": 8

    }

    @staticmethod
    def analyze(question: str):

        question = question.lower()

        score = 0
        matched = []

        for keyword, weight in EscalationEngine.keyword_weights.items():

            if keyword in question:

                matched.append(keyword)
                score += weight

        # Extra rule
        if "payment" in question and "deducted" in question:
            score += 5
            matched.append("payment deducted")

        if "order" in question and "not confirmed" in question:
            score += 5
            matched.append("order not confirmed")

        if score >= 8:
            priority = "HIGH"
            escalate = True

        elif score >= 4:
            priority = "MEDIUM"
            escalate = False

        else:
            priority = "LOW"
            escalate = False

        return {

            "priority": priority,
            "escalate": escalate,
            "score": score,
            "matched_keywords": matched

        }