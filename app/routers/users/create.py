from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.users.user_query import UserQuery
from app.infrastructure.dto.users.user_create_command import UserCreateCommand
from app.infrastructure.repositories.users_repository import UsersRepository
from app.use_cases.get_user import get_current_admin_user
from app.use_cases.hashing import get_password_hash


async def add_user(request_body: UserCreateCommand, user_data: User = Depends(get_current_admin_user)) -> UserQuery:
    request_body.password = get_password_hash(request_body.password)
    try:
        user = await UsersRepository.add(**request_body.model_dump())
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
