from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.users.change_pass_command import ChangePassCommand
from app.infrastructure.repositories.users_repository import UsersRepository
from app.use_cases.get_user import get_current_user
from app.use_cases.hashing import get_password_hash


async def change_pass(request_body: ChangePassCommand, user_data: User = Depends(get_current_user)):
    is_correct_code = await UsersRepository.check_code(request_body.code)
    if not is_correct_code:
        raise HTTPException(status_code=403, detail="incorrect code")

    request_body.password = get_password_hash(request_body.password)
    try:
        user = await UsersRepository.update({"id": user_data.id}, **{"password": request_body.password})
        if user is None:
            raise HTTPException(status_code=404, detail="user not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
