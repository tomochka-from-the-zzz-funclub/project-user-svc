from fastapi import Depends

from app.domain.models.user import User
from app.use_cases.get_user import get_current_user


async def send_code(user_data: User = Depends(get_current_user)):
    return
