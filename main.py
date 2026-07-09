from fastapi import FastAPI
from core.database import connect_to_mongo, close_mongo_connection
from router.auth import router as auth_router
from router.user import router as user_router


from core.database import (
    connect_to_mongo,
    close_mongo_connection
)

app = FastAPI()


@app.on_event("startup")
async def startup():

    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown():

    await close_mongo_connection()


@app.get("/")
async def root():

    return {
        "message": "Customer Support AI Backend Running"
    }
app.include_router(auth_router)
app.include_router(user_router)
