from pydantic import EmailStr

from app.infrastructure.repositories.user_repository import UserRepository
from app.use_cases.hashing import verify_password


async def authenticate_user(email: EmailStr, password: str):
    user = await UserRepository.find_one_or_none(email=email)
    if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
        return None
    return user