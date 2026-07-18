import time

from rag.retriver import Retriever
from rag.prompt_builder import PromptBuilder
from llm.gemini import GeminiClient


class RAGPipeline:

    @staticmethod
    def ask(

        question: str,

        history: list,

        agent_context: str

    ):

        total_start = time.perf_counter()

        # ------------------------------------
        # Retriever
        # ------------------------------------

        t1 = time.perf_counter()

        documents = Retriever.retrieve(question)

        t2 = time.perf_counter()

        print(f"[Retriever] {(t2 - t1):.2f} sec")

        # ------------------------------------
        # Context
        # ------------------------------------

        context = "\n\n".join(

            [

                doc.page_content

                for doc in documents

            ]

        )

        # ------------------------------------
        # Prompt Builder
        # ------------------------------------

        t3 = time.perf_counter()

        prompt = PromptBuilder.build(

            history=history,

            context=context,

            agent_context=agent_context,

            question=question

        )

        t4 = time.perf_counter()

        print(f"[Prompt Builder] {(t4 - t3):.2f} sec")

        # Optional: prompt size check
        print(f"[Prompt Length] {len(prompt)} characters")

        # ------------------------------------
        # Gemini
        # ------------------------------------

        model = GeminiClient.get_model()

        t5 = time.perf_counter()

        response = model.generate_content(prompt)

        t6 = time.perf_counter()

        print(f"[Gemini] {(t6 - t5):.2f} sec")

        total_end = time.perf_counter()

        print("=" * 60)
        print(f"[TOTAL RAG] {(total_end - total_start):.2f} sec")
        print("=" * 60)

        return response.text