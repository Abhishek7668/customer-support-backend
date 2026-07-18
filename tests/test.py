import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.escalation import EscalationEngine


queries = [

    "My payment failed.",

    "My payment is still not working.",

    "Worst service. I want refund.",

    "I am angry. This is fraud. I want manager.",

    "Everything is working."

]

for q in queries:

    print("="*70)

    print(q)

    print(

        EscalationEngine.analyze(q)

    )