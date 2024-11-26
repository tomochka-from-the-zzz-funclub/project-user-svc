from typing import Dict

from fastapi import Depends, HTTPException, status, Response

from app.domain.models.user import User
from app.infrastructure.dto.users.user_create_command import UserCreateCommand
from app.infrastructure.dto.users.user_auth_query import UserAuthQuery
from app.infrastructure.repositories.users_repository import UsersRepository
from app.use_cases.hashing import get_password_hash
from app.use_cases.jwt import create_access_token
from app.use_cases.authenticate import authenticate_user
from app.use_cases.get_user import get_current_user


async def register_user(response: Response, user_data: UserCreateCommand) -> Dict:
    response.delete_cookie(key="users_access_token")
    users = await UsersRepository.find_by_filter(email=user_data.email)
    if len(users) > 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    user = await UsersRepository.add(**user_dict)

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

async def auth_user(response: Response, user_data: UserAuthQuery) -> Dict:
    print("auth_user: start")
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    response.delete_cookie(key="users_access_token")
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

async def logout_user(response: Response, user_data: User = Depends(get_current_user)) -> Dict:
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}
