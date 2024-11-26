from fastapi import Depends

from app.domain.models.user import User
from app.infrastructure.dto.favorite_films.film_query import FilmQuery
from app.infrastructure.repositories.favorite_films_repository import FavoriteFilmsRepository
from app.use_cases.get_user import get_current_user


async def get_films(user_data: User = Depends(get_current_user)) -> list[FilmQuery]:
    return await FavoriteFilmsRepository.find_by_filter(**{"user_id": user_data.id})
