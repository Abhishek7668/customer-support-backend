import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auth.password import hash_password, verify_password

pwd = hash_password("admin123")
print(pwd)

print(verify_password("admin123", pwd))