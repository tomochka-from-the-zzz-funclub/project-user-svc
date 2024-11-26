from app.infrastructure.db.models.viewed import Viewed
from app.infrastructure.repositories.repository import Repository

class ViewedRepository(Repository):
    model = Viewed
