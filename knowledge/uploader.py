from rag.pincone_store import PineconeStore


class KnowledgeUploader:

    @staticmethod
    def upload(chunks):

        vector_store = PineconeStore.get_vector_store()

        vector_store.add_documents(chunks)

        return {

            "success": True,

            "total_chunks": len(chunks),

            "message": "Knowledge uploaded successfully."

        }