# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer

# from auth.jwt_handler import verify_access_token
# from repositry.user_repositry import UserRepository

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# async def get_current_user(
#     token: str = Depends(oauth2_scheme)
# ):

#     payload = verify_access_token(token)

#     if payload is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or Expired Token"
#         )

#     user = await UserRepository.get_by_email(
#         payload["email"]
#     )

#     if user is None:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not Found"
#         )

#     return user

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from auth.jwt_handler import verify_access_token

security = HTTPBearer()


async def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security)

):

    token = credentials.credentials

    payload = verify_access_token(token)

    if payload is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid Token"

        )

    return payload