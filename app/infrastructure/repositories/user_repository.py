from app.infrastructure.db.models.users import User
from app.infrastructure.repositories.repository import Repository

class UserRepository(Repository):
    model = User
