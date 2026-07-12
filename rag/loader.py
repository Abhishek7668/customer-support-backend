from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)

    def load(self):

        documents = []

        pdf_files = list(self.folder_path.glob("*.pdf"))

        if not pdf_files:
            raise Exception("No PDF Found")

        for pdf in pdf_files:

            loader = PyPDFLoader(str(pdf))

            documents.extend(loader.load())

        return documents