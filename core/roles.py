from enum import Enum


class UserRole(str, Enum):

    ADMIN = "admin"

    SUPPORT_MANAGER = "support_manager"

    SUPPORT_AGENT = "support_agent"

    CUSTOMER = "customer"