from auth.password import hash_password, verify_password
from auth.jwt_handler import create_access_token
from models.user_model import create_user_document
from repositry.user_repositry import UserRepository


class AuthService:

    @staticmethod
    async def register(user):

        existing = await UserRepository.get_by_email(user.email)

        if existing:
            raise Exception("Email already exists")

        hashed = hash_password(user.password)

        document = create_user_document(user, hashed)

        user_id = await UserRepository.create(document)

        return str(user_id)


    @staticmethod
    async def login(user):

        db_user = await UserRepository.get_by_email(user.email)

        if not db_user:
            raise Exception("Invalid Email")

        if not verify_password(
            user.password,
            db_user["password"]
        ):
            raise Exception("Invalid Password")

        token = create_access_token(
            {
                "sub": str(db_user["_id"]),
                "email": db_user["email"],
                "role": db_user["role"]
            }
        )

        return token