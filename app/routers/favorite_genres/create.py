from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.favorite_genres.genre_query import GenreQuery
from app.infrastructure.dto.favorite_genres.genre_create_command import GenreCreateCommand
from app.infrastructure.repositories.favorite_genres_repository import FavoriteGenresRepository
from app.use_cases.get_user import get_current_user


async def add_genre(request_body: GenreCreateCommand, user_data: User = Depends(get_current_user)) -> GenreQuery:
    try:
        dict_ = request_body.model_dump()
        dict_["user_id"] = user_data.id
        genre = await FavoriteGenresRepository.add(**dict_)
        return genre
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
