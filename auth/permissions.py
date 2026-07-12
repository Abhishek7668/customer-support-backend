from fastapi import Depends, HTTPException

from auth.dependency import get_current_user


def require_roles(*roles):

    async def checker(

        current_user=Depends(get_current_user)

    ):

        if current_user["role"] not in roles:

            raise HTTPException(

                status_code=403,

                detail="Permission Denied"

            )

        return current_user

    return checker