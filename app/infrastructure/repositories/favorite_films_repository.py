from app.infrastructure.db.models.favorite_films import FavoriteFilm
from app.infrastructure.repositories.repository import Repository

class FavoriteFilmsRepository(Repository):
    model = FavoriteFilm
