from knowledge.loader import PDFLoader
from knowledge.chunker import DocumentChunker
from knowledge.uploader import KnowledgeUploader


class KnowledgeService:

    @staticmethod
    def upload(pdf_path: str):

        # ---------------------------------
        # Load PDF
        # ---------------------------------

        documents = PDFLoader.load(

            pdf_path

        )

        # ---------------------------------
        # Split into Chunks
        # ---------------------------------

        chunks = DocumentChunker.split(

            documents

        )

        # ---------------------------------
        # Upload to Pinecone
        # ---------------------------------

        result = KnowledgeUploader.upload(

            chunks

        )

        return {

            "success": True,

            "pdf": pdf_path.split("\\")[-1],

            "pages": len(documents),

            "chunks": len(chunks),

            "message": result["message"]

        }