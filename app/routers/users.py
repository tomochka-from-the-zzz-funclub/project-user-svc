from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status, Response
from app.domain.models.user import User
from app.infrastructure.dto.user_query import UserQuery
from app.infrastructure.dto.user_create_command import UserCreateCommand
from app.infrastructure.dto.user_filter_query import UserFilterQuery
from app.infrastructure.dto.user_auth_query import UserAuthQuery
from app.infrastructure.repositories.user_repository import UserRepository

from app.use_cases.hashing import get_password_hash
from app.use_cases.jwt import create_access_token
from app.use_cases.authenticate import authenticate_user
from app.use_cases.jwt import get_current_user
from app.use_cases.jwt import get_current_admin_user

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей", response_model=list[UserQuery])
async def get_all_users(user_data: User = Depends(get_current_admin_user)):
    return await UserRepository.find_all()

@router.post("/", summary="Создание пользователя")
async def add_user(request_body: UserCreateCommand, user_data: User = Depends(get_current_admin_user)) -> UserQuery:
    try:
        user = await UserRepository.add(**request_body.model_dump())
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/by_filter", summary="Получить одного пользователя с фильтрацией")
async def get_user_by_filter(request_body: UserFilterQuery = Depends(), user_data: User = Depends(get_current_admin_user)) -> UserQuery:
    user = await UserRepository.find_one_or_none(**request_body.to_dict())
    if user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user


# Аутентификация Авторизация

@router.post("/register")
async def register_user(response: Response, user_data: UserCreateCommand) -> Dict:
    response.delete_cookie(key="users_access_token")
    user = await UserRepository.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    user =  await UserRepository.add(**user_dict)

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

@router.post("/login")
async def auth_user(response: Response, user_data: UserAuthQuery) -> Dict:
    response.delete_cookie(key="users_access_token")
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

@router.get("/me")
async def get_me(user_data: User = Depends(get_current_user)) -> UserQuery:
    return user_data

@router.post("/logout")
async def logout_user(response: Response, user_data: User = Depends(get_current_user)):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@router.get("/{user_id}", summary="Получить одного пользователя по id")
async def get_user_by_id(user_id: int, user_data: User = Depends(get_current_admin_user)) -> UserQuery:
    user = await UserRepository.find_one_or_none_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user