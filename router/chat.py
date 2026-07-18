from fastapi import APIRouter, Depends

from schema.chat_schema import ChatRequest
from services.chat_services import ChatService

from auth.jwt_beare import get_current_user

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("")
async def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user)
):

    result = await ChatService.chat(

        user_id=current_user["sub"],

        session_id=request.session_id,

        question=request.question

    )

    return {

        "success": True,

        **result

    }