print("========== 11. pincone_store.py loaded ==========")

from langchain_pinecone import PineconeVectorStore

print("========== 12. langchain_pinecone imported ==========")

from rag.embeddings import EmbeddingModel

print("========== 13. EmbeddingModel imported ==========")

from core.config import settings

print("========== 14. settings imported ==========")


class PineconeStore:

    _vector_store = None

    @classmethod
    def get_vector_store(cls):

        print("========== Creating Vector Store ==========")

        if cls._vector_store is None:

            embeddings = EmbeddingModel.get_embeddings()

            print("========== Embeddings Loaded ==========")

            cls._vector_store = PineconeVectorStore(
                index_name=settings.PINECONE_INDEX,
                embedding=embeddings,
                pinecone_api_key=settings.PINECONE_API_KEY
            )

            print("========== Pinecone Connected ==========")

        return cls._vector_store