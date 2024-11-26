from fastapi import Depends

from app.domain.models.user import User
from app.infrastructure.dto.viewed.viewed_query import ViewedQuery
from app.infrastructure.repositories.viewed_repository import ViewedRepository
from app.use_cases.get_user import get_current_user


async def get_viewed(user_data: User = Depends(get_current_user)) -> list[ViewedQuery]:
    return await ViewedRepository.find_by_filter(**{"user_id": user_data.id})
