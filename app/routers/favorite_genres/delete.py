from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.repositories.favorite_genres_repository import FavoriteGenresRepository
from app.use_cases.get_user import get_current_user


async def delete_genre(genre_id: int, user_data: User = Depends(get_current_user)) -> bool:
    dict_ = {
        "user_id": user_data.id,
        "genre_id": genre_id
    }
    row_count = await FavoriteGenresRepository.delete(delete_all=False, **dict_)

    if row_count > 0:
        return True
    else:
        raise HTTPException(status_code=404, detail="Genre not found")
