from fastapi import Depends, HTTPException, Path, Body

from app.domain.models.user import User
from app.infrastructure.dto.users.user_query import UserQuery
from app.infrastructure.dto.users.user_update_command import UserUpdateCommand
from app.infrastructure.repositories.users_repository import UsersRepository
from app.use_cases.get_user import get_current_user
from app.use_cases.get_user import get_current_admin_user


async def update(user_id: int, request_body: UserUpdateCommand):
    try:
        user = await UsersRepository.update({"id": user_id}, **request_body.model_dump(exclude_none=True))
        if user is None:
            raise HTTPException(status_code=404, detail="user not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def update_user_by_id(user_id: int = Path(...), request_body: UserUpdateCommand = Body(...), user_data: User = Depends(get_current_admin_user)) -> UserQuery:
    return await update(user_id, request_body)

async def update_user(request_body: UserUpdateCommand, user_data: User = Depends(get_current_user)) -> UserQuery:
    return await update(user_data.id, request_body)
