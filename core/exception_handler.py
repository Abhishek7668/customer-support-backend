from fastapi import FastAPI
from fastapi.responses import JSONResponse

from expections.auth_exception import *


def register_exception(app: FastAPI):

    @app.exception_handler(EmailAlreadyExists)
    async def email_exist(_, exc):

        return JSONResponse(

            status_code=400,

            content={

                "success": False,

                "message": str(exc)

            }

        )

    @app.exception_handler(InvalidCredentials)
    async def invalid(_, exc):

        return JSONResponse(

            status_code=401,

            content={

                "success": False,

                "message": str(exc)

            }

        )