from fastapi import APIRouter

from app.infrastructure.dto.favorite_genres.genre_query import GenreQuery
from app.routers.favorite_genres.create import add_genre
from app.routers.favorite_genres.read import get_genres
from app.routers.favorite_genres.delete import delete_genre

router = APIRouter(prefix='/favorite_genres', tags=['Работа с избранными жанрами от имени авторизованного пользователя'])

router.add_api_route("/", add_genre, methods=["POST"], summary="Добавление избранного фильма", response_model=GenreQuery)

router.add_api_route("/", get_genres, methods=["GET"], summary="Получить все избранные фильмы", response_model=list[GenreQuery])

router.add_api_route("/{genre_id}", delete_genre, methods=["DELETE"], summary="Удаление избранного фильма", response_model=bool)
