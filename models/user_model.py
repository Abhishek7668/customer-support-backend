from datetime import datetime
from core.roles import UserRole


def create_user_document(user, hashed_password):
    return {
        "full_name": user.full_name,
        "email": user.email.lower(),
        "password": hashed_password,
        "role": UserRole.CUSTOMER.value,
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }