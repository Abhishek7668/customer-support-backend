from fastapi import APIRouter, Depends

from auth.jwt_beare import get_current_user
from services.conversation_service import ConversationService

router = APIRouter(
    prefix="/history",
    tags=["Conversation History"]
)


@router.get("/{session_id}")
async def history(

    session_id: str,

    current_user=Depends(get_current_user)

):

    history = await ConversationService.history(

        user_id=current_user["sub"],

        session_id=session_id

    )

    return {

        "success": True,

        "history": history

    }