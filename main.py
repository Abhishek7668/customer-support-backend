# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from core.database import connect_to_mongo, close_mongo_connection

# from router.auth import router as auth_router
# from router.user import router as user_router
# from router.chat import router as chat_router
# from router.history import router as history_router
# from router.analytics import router as analytics_router
# from router.ticket import router as ticket_router
# from router.knowledge import router as knowledge_router

# # -----------------------------
# # AI Preload Imports
# # -----------------------------
# from rag.embeddings import EmbeddingModel
# from rag.pincone_store import PineconeStore
# from llm.gemini import GeminiClient

# app = FastAPI()

# app = FastAPI()

# # -----------------------------
# # CORS Configuration
# # -----------------------------
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.on_event("startup")
# async def startup():

#     #print("=" * 60)
#     print("Starting Customer Support AI Backend")
#     #print("=" * 60)
#     :

#     print("Starting Backend...")

#     await connect_to_mongo()

#     print("MongoDB Connected")

#     # MongoDB
#    # await connect_to_mongo()
#    # print("MongoDB Connected")

#     ## Embedding Model
#    # EmbeddingModel.get_embeddings()
#    # print("Embedding Model Loaded")

#     # Pinecone
#    # PineconeStore.get_vector_store()
#    # print("Pinecone Connected")

#     # Gemini
#    # GeminiClient.get_model()
#    #print("Gemini Loaded")

#    #print("=" * 60)
#    # print("Backend Ready")
#    # print("=" * 60)


# @app.on_event("shutdown")
# async def shutdown():

#     await close_mongo_connection()

#     print("MongoDB Closed")


# @app.get("/")
# async def root():

#     return {

#         "message": "Customer Support AI Backend Running"

#     }


# app.include_router(auth_router)
# app.include_router(user_router)
# app.include_router(chat_router)
# app.include_router(history_router)
# app.include_router(analytics_router)
# app.include_router(ticket_router)
# app.include_router(knowledge_router)




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.database import connect_to_mongo, close_mongo_connection

# Safe Routers
from router.auth import router as auth_router
from router.user import router as user_router
from router.history import router as history_router
from router.ticket import router as ticket_router
from router.analytics import router as analytics_router
from router.knowledge import router as knowledge_router
print("Knowledg IMport success")

# Chat Router (abhi disable)
# from router.chat import router as chat_router

app = FastAPI(
    title="Customer Support AI Backend",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("=" * 60)
    print("Starting Customer Support AI Backend")
    print("=" * 60)

    try:
        await connect_to_mongo()
        print("✅ MongoDB Connected Successfully")
    except Exception as e:
        print(f"❌ MongoDB Connection Failed: {e}")
        raise

    print("=" * 60)
    print("Backend Ready")
    print("=" * 60)

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()
    print("MongoDB Closed")

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Customer Support AI Backend Running"
    }

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(history_router)
app.include_router(ticket_router)
app.include_router(analytics_router)
app.include_router(knowledge_router)

# Last step
# app.include_router(chat_router)