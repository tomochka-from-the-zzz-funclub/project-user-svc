from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.favorite_films.film_query import FilmQuery
from app.infrastructure.dto.favorite_films.film_create_command import FilmCreateCommand
from app.infrastructure.repositories.favorite_films_repository import FavoriteFilmsRepository
from app.use_cases.get_user import get_current_user


async def add_film(request_body: FilmCreateCommand, user_data: User = Depends(get_current_user)) -> FilmQuery:
    try:
        dict_ = request_body.model_dump()
        dict_["user_id"] = user_data.id
        film = await FavoriteFilmsRepository.add(**dict_)
        return film
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
