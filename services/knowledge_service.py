print("========== 5. knowledge_service.py loaded ==========")

from knowledge.loader import PDFLoader
print("========== 6. PDFLoader imported ==========")

from knowledge.chunker import DocumentChunker
print("========== 7. DocumentChunker imported ==========")

from knowledge.uploader import KnowledgeUploader
print("========== 8. KnowledgeUploader imported ==========")


class KnowledgeService:

    @staticmethod
    def upload(pdf_path: str):

        print("========== Loading PDF ==========")

        documents = PDFLoader.load(pdf_path)

        print("========== Splitting Chunks ==========")

        chunks = DocumentChunker.split(documents)

        print("========== Uploading To Pinecone ==========")

        result = KnowledgeUploader.upload(chunks)

        print("========== Upload Finished ==========")

        return {
            "success": True,
            "pdf": pdf_path.split("\\")[-1],
            "pages": len(documents),
            "chunks": len(chunks),
            "message": result["message"]
        }