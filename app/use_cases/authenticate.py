from pydantic import EmailStr

from app.infrastructure.repositories.users_repository import UsersRepository
from app.use_cases.hashing import verify_password


async def authenticate_user(email: EmailStr, password: str):
    users = await UsersRepository.find_by_filter(email=email)
    if len(users) == 0:
        print("authenticate_user: not found users")
        return None

    user = users[0]
    if verify_password(plain_password=password, hashed_password=user.password) is False:
        print("authenticate_user: incorrect password")
        return None
    return user
