# 
from fastapi import APIRouter, Depends

from auth.dependency import get_current_user

router = APIRouter(

    prefix="/users",

    tags=["Users"]

)


@router.get("/me")
async def me(

    current_user=Depends(get_current_user)

):

    return {

        "success": True,

        "data": current_user

    }