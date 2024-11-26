from fastapi import APIRouter

from app.infrastructure.dto.favorite_films.film_query import FilmQuery
from app.routers.favorite_films.create import add_film
from app.routers.favorite_films.read import get_films
from app.routers.favorite_films.delete import delete_film

router = APIRouter(prefix='/favorite_films', tags=['Работа с избранными фильмами от имени авторизованного пользователя'])

router.add_api_route("/", add_film, methods=["POST"], summary="Добавление избранного фильма", response_model=FilmQuery)

router.add_api_route("/", get_films, methods=["GET"], summary="Получить все избранные фильмы", response_model=list[FilmQuery])

router.add_api_route("/{film_id}", delete_film, methods=["DELETE"], summary="Удаление избранного фильма", response_model=bool)
