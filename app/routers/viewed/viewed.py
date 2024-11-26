from fastapi import APIRouter

from app.infrastructure.dto.viewed.viewed_query import ViewedQuery
from app.routers.viewed.create import add_viewed
from app.routers.viewed.read import get_viewed
from app.routers.viewed.update import update_viewed
from app.routers.viewed.delete import delete_viewed

router = APIRouter(prefix='/viewed', tags=['Работа с просмотренными фильмами от имени авторизованного пользователя'])

router.add_api_route("/", add_viewed, methods=["POST"], summary="Добавление просмотренного фильма", response_model=ViewedQuery)

router.add_api_route("/", get_viewed, methods=["GET"], summary="Получить все просмотренные фильмы", response_model=list[ViewedQuery])

router.add_api_route("/{film_id}", update_viewed, methods=["PUT"], summary="Удаление просмотренного фильма", response_model=ViewedQuery)

router.add_api_route("/{film_id}", delete_viewed, methods=["DELETE"], summary="Удаление просмотренного фильма", response_model=bool)
