from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, timezone
from app.config import get_auth_data
from app.infrastructure.repositories.users_repository import UsersRepository
from app.domain.models.user import User
from app.use_cases.jwt import get_token


async def get_current_user(token: str = Depends(get_token)):
    print("get_current_user: start")
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=[auth_data['algorithm']])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен не валидный!')

    expire = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен истек')

    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не найден ID пользователя')

    user = await UsersRepository.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')

    return user

async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    print("get_current_admin_user: start")
    if current_user.is_admin:
        return current_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Недостаточно прав!')
