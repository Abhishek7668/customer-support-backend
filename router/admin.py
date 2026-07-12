from fastapi import APIRouter, Depends

from auth.permissions import require_roles

router = APIRouter()


@router.get("/admin")

async def admin_dashboard(

    user=Depends(

        require_roles("admin")

    )

):

    return {

        "message":"Welcome Admin"

    }