from fastapi import APIRouter

from app.infrastructure.dto.users.user_query import UserQuery
from app.routers.users.auth import register_user, auth_user, logout_user
from app.routers.users.create import add_user
from app.routers.users.read import get_all_users, get_users_by_filter, get_me, get_user_by_id
from app.routers.users.update import update_user, update_user_by_id
from app.routers.users.change_pass import change_pass
from app.routers.users.send_code import send_code

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

router.add_api_route("/register", register_user, methods=["POST"])
router.add_api_route("/login", auth_user, methods=["POST"])
router.add_api_route("/logout", logout_user, methods=["GET"])

router.add_api_route("/", add_user, methods=["POST"], summary="Создание пользователя", response_model=UserQuery)

router.add_api_route("/", get_all_users, methods=["GET"], summary="Получить всех пользователей", response_model=list[UserQuery])
router.add_api_route("/by_filter", get_users_by_filter, methods=["GET"], summary="Получить пользователей с фильтрацией", response_model=list[UserQuery])
router.add_api_route("/me", get_me, methods=["GET"], response_model=UserQuery)

router.add_api_route("/", update_user, methods=["PUT"], summary="Обновить информацию о себе", response_model=UserQuery)

router.add_api_route("/change_pass", change_pass, methods=["PUT"], summary="Обновить пароль")

router.add_api_route("/get_code", send_code, methods=["GET"], summary="Получить код подтверждения")

router.add_api_route("/{user_id}", get_user_by_id, methods=["GET"], summary="Получить одного пользователя по id", response_model=UserQuery)
router.add_api_route("/{user_id}", update_user_by_id, methods=["PUT"], summary="Обновить информацию о пользователе по id", response_model=UserQuery)
