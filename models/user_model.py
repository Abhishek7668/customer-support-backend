from datetime import datetime


def create_user_document(user, hashed_password):
    return {
        "full_name": user.full_name,
        "email": user.email.lower(),
        "password": hashed_password,
        "role": "customer",
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }