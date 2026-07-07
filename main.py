from fastapi import FastAPI
from core.database import connect_to_mongo, close_mongo_connection

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
