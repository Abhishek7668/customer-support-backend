import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.loader import PDFLoader
from rag.text_spliter import TextSplitter
from rag.pincone_store import PineconeStore

print("=" * 60)
print("Loading PDFs...")
print("=" * 60)

loader = PDFLoader(r"D:\project 2\customer-support-backend\knowledge_base")

documents = loader.load()

print(f"Loaded Pages : {len(documents)}")

print("=" * 60)
print("Chunking...")
print("=" * 60)

chunks = TextSplitter.split_documents(documents)

print(f"Total Chunks : {len(chunks)}")

print("=" * 60)
print("Uploading to Pinecone...")
print("=" * 60)

vector_store = PineconeStore.get_vector_store()

vector_store.add_documents(chunks)

print("=" * 60)
print("Upload Completed Successfully")
print("=" * 60)