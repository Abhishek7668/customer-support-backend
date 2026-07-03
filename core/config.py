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

print("Creating settings...")
settings = Settings()
print("Settings created!")