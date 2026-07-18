from langchain_pinecone import PineconeVectorStore
from rag.embeddings import EmbeddingModel
from core.config import settings


class PineconeStore:

    _vector_store = None

    @classmethod
    def get_vector_store(cls):

        if cls._vector_store is None:

            embeddings = EmbeddingModel.get_embeddings()

            cls._vector_store = PineconeVectorStore(
                index_name=settings.PINECONE_INDEX,
                embedding=embeddings,
                pinecone_api_key=settings.PINECONE_API_KEY
            )

        # 👇 Always return
        return cls._vector_store