# from langchain_community.document_loaders import PyPDFLoader


# class PDFLoader:

#     @staticmethod
#     def load(pdf_path: str):

#         loader = PyPDFLoader(pdf_path)

#         documents = loader.load()

#         return documents

print("===== loader.py started =====")

from langchain_community.document_loaders import PyPDFLoader

print("===== PyPDFLoader imported =====")


class PDFLoader:

    @staticmethod
    def load(pdf_path: str):

        print("===== Inside PDFLoader.load() =====")

        loader = PyPDFLoader(pdf_path)

        print("===== PyPDFLoader object created =====")

        documents = loader.load()

        print("===== PDF loaded =====")

        return documents