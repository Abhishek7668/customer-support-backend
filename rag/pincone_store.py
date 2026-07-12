from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from core.config import settings
from rag.embeddings import EmbeddingModel


class PineconeStore:

    @staticmethod
    def get_vector_store():

        pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )

        embeddings = EmbeddingModel.get_embeddings()

        vector_store = PineconeVectorStore(
            index_name=settings.PINECONE_INDEX,
            embedding=embeddings,
            pinecone_api_key=settings.PINECONE_API_KEY
        )

        return vector_store