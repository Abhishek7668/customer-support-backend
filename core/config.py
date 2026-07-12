from dotenv import load_dotenv
import os

print("Loading config...")

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    DEBUG = os.getenv("DEBUG") == "True"
    MONGO_URI = os.getenv("MONGO_URI")

    DB_NAME = os.getenv("DB_NAME")
    SECRET_KEY=os.getenv("SECRET_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")
print("Creating settings...")
settings = Settings()
print("Settings created!")