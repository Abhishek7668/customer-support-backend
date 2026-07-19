# print("========== 5. knowledge_service.py loaded ==========")

# from knowledge.loader import PDFLoader
# print("========== 6. PDFLoader imported ==========")

# from knowledge.chunker import DocumentChunker
# print("========== 7. DocumentChunker imported ==========")

# from knowledge.uploader import KnowledgeUploader
# print("========== 8. KnowledgeUploader imported ==========")


# class KnowledgeService:

#     @staticmethod
#     def upload(pdf_path: str):

#         print("========== Loading PDF ==========")

#         documents = PDFLoader.load(pdf_path)

#         print("========== Splitting Chunks ==========")

#         chunks = DocumentChunker.split(documents)

#         print("========== Uploading To Pinecone ==========")

#         result = KnowledgeUploader.upload(chunks)

#         print("========== Upload Finished ==========")

#         return {
#             "success": True,
#             "pdf": pdf_path.split("\\")[-1],
#             "pages": len(documents),
#             "chunks": len(chunks),
#             "message": result["message"]
#         }

from knowledge.loader import PDFLoader


class KnowledgeService:

    @staticmethod
    def upload(pdf_path: str):

        try:

            print("=" * 60)
            print("KnowledgeService Started")
            print(f"PDF Path : {pdf_path}")
            print("=" * 60)

            # Load PDF
            documents = PDFLoader.load(pdf_path)

            print(f"Documents Loaded : {len(documents)}")

            return {
                "success": True,
                "message": "PDF Loaded Successfully",
                "total_documents": len(documents)
            }

        except Exception as e:

            print("=" * 60)
            print("KnowledgeService Error")
            print(str(e))
            print("=" * 60)

            return {
                "success": False,
                "message": str(e)
            }