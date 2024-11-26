from app.infrastructure.db.models.users import User
from app.infrastructure.repositories.repository import Repository

class UsersRepository(Repository):
    model = User
