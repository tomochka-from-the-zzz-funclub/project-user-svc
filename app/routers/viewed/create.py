from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.viewed.viewed_query import ViewedQuery
from app.infrastructure.dto.viewed.viewed_create_command import ViewedCreateCommand
from app.infrastructure.repositories.viewed_repository import ViewedRepository
from app.use_cases.get_user import get_current_user


async def add_viewed(request_body: ViewedCreateCommand, user_data: User = Depends(get_current_user)) -> ViewedQuery:
    try:
        dict_ = request_body.model_dump()
        dict_["user_id"] = user_data.id
        film = await ViewedRepository.add(**dict_)
        return film
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
