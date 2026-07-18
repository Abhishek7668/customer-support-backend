from rag.pincone_store import PineconeStore


class Retriever:

    _vector_store = None

    @classmethod
    def retrieve(

        cls,

        query: str,

        k: int = 5

    ):

        if cls._vector_store is None:

            cls._vector_store = PineconeStore.get_vector_store()

        documents = cls._vector_store.similarity_search(

            query=query,

            k=k

        )

        return documents