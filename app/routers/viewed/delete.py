from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.repositories.viewed_repository import ViewedRepository
from app.use_cases.get_user import get_current_user


async def delete_viewed(film_id: int, user_data: User = Depends(get_current_user)) -> bool:
    dict_ = {
        "user_id": user_data.id,
        "film_id": film_id
    }
    row_count = await ViewedRepository.delete(delete_all=False, **dict_)

    if row_count > 0:
        return True
    else:
        raise HTTPException(status_code=404, detail="Viewed not found")
