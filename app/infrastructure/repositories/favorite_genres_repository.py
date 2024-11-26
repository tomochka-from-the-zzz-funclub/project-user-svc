from app.infrastructure.db.models.favorite_genres import FavoriteGenre
from app.infrastructure.repositories.repository import Repository

class FavoriteGenresRepository(Repository):
    model = FavoriteGenre
