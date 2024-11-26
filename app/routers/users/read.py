from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.users.user_query import UserQuery
from app.infrastructure.dto.users.user_filter_query import UserFilterQuery
from app.infrastructure.repositories.users_repository import UsersRepository
from app.use_cases.get_user import get_current_user
from app.use_cases.get_user import get_current_admin_user


async def get_all_users(user_data: User = Depends(get_current_admin_user)) -> list[UserQuery]:
    return await UsersRepository.find_all()

async def get_user_by_id(user_id: int, user_data: User = Depends(get_current_admin_user)) -> UserQuery:
    print("get_user_by_id: start")
    user = await UsersRepository.find_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user

async def get_users_by_filter(request_body: UserFilterQuery = Depends(), user_data: User = Depends(get_current_admin_user)) -> list[UserQuery]:
    print("get_user_by_filter: start")
    return await UsersRepository.find_by_filter(**request_body.to_dict())

async def get_me(user_data: User = Depends(get_current_user)) -> UserQuery:
    print("get_user_by_filter: start")
    return user_data
