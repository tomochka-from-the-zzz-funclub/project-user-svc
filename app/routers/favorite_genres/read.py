from fastapi import Depends

from app.domain.models.user import User
from app.infrastructure.dto.favorite_genres.genre_query import GenreQuery
from app.infrastructure.repositories.favorite_genres_repository import FavoriteGenresRepository
from app.use_cases.get_user import get_current_user


async def get_genres(user_data: User = Depends(get_current_user)) -> list[GenreQuery]:
    return await FavoriteGenresRepository.find_by_filter(**{"user_id": user_data.id})
