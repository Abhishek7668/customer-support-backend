# from langchain_community.document_loaders import PyPDFLoader


# class PDFLoader:

#     @staticmethod
#     def load(pdf_path: str):

#         loader = PyPDFLoader(pdf_path)

#         documents = loader.load()

#         return documents

from pypdf import PdfReader
from langchain_core.documents import Document


class PDFLoader:

    @staticmethod
    def load(pdf_path: str):
        reader = PdfReader(pdf_path)

        documents = []

        for page in reader.pages:
            text = page.extract_text() or ""
            documents.append(
                Document(page_content=text)
            )

        return documents