# print("========== 9. uploader.py loaded ==========")

# from rag.pincone_store import PineconeStore

# print("========== 10. PineconeStore imported ==========")


# class KnowledgeUploader:

#     @staticmethod
#     def upload(chunks):

#         print("========== Getting Vector Store ==========")

#         vector_store = PineconeStore.get_vector_store()

#         print("========== Vector Store Ready ==========")

#         vector_store.add_documents(chunks)

#         print("========== Documents Added ==========")

#         return {
#             "success": True,
#             "total_chunks": len(chunks),
#             "message": "Knowledge uploaded successfully."
#         }

print("Uploader loaded")

class KnowledgeUploader:

    @staticmethod
    def upload(chunks):
        return {
            "success": True,
            "total_chunks": len(chunks),
            "message": "Temporary success"
        }