from fastapi import APIRouter, HTTPException

from schema.user_schema import UserRegister , UserLogin
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
async def register(user: UserRegister):

    try:

        user_id = await AuthService.register(user)

        return {
            "success": True,
            "message": "User registered successfully",
            "user_id": user_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
@router.post("/login")
async def login(user: UserLogin):

    try:

        token = await AuthService.login(user)

        return {
            "success": True,
            "access_token": token,
            "token_type": "Bearer"
        }

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )