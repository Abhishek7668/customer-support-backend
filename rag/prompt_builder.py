class PromptBuilder:

    @staticmethod
    def build(

        history,

        context,

        agent_context,

        question

    ):

        conversation = ""

        for chat in history:

            conversation += f"""

User:

{chat['question']}

Assistant:

{chat['answer']}

"""

        prompt = f"""

You are an Enterprise AI Customer Support Assistant.

==================================================

Previous Conversation

{conversation}

==================================================

Specialized Agent Analysis

{agent_context}

==================================================

Company Knowledge

{context}

==================================================

Current Customer Question

{question}

==================================================

Instructions

1. Use Company Knowledge first.

2. Use Agent Analysis.

3. Use Previous Conversation if relevant.

Response Guidelines

1. Keep answers concise (100-200 words) unless the user explicitly asks for detailed information.
2. Use bullet points whenever possible.
3. For recommendation questions, recommend the best option first, then mention alternatives.
4. End every answer with a short follow-up question if appropriate.
5. Avoid long paragraphs.
6. Use company knowledge only.
7. Never invent information.

5. Never mention Billing Agent,
Technical Agent,
Complaint Agent,
or internal processing.

"""

        return prompt