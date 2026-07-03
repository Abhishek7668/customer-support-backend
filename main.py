from fastapi import FastAPI

from core.config import settings

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION

)


@app.get("/")

def home():

    return {

        "message": settings.APP_NAME,

        "version": settings.APP_VERSION

    }


@app.get("/health")

def health():

    return {

        "status": "healthy"

    }