from fastapi import HTTPException, Depends

from app.domain.models.user import User
from app.infrastructure.dto.viewed.viewed_query import ViewedQuery
from app.infrastructure.dto.viewed.viewed_update_command import ViewedUpdateCommand
from app.infrastructure.repositories.viewed_repository import ViewedRepository
from app.use_cases.get_user import get_current_user


async def update_viewed(film_id: int, request_body: ViewedUpdateCommand, user_data: User = Depends(get_current_user)) -> ViewedQuery:
    try:
        dict_ = {
            "user_id": user_data.id,
            "film_id": film_id
        }
        viewed = await ViewedRepository.update(dict_, **request_body.model_dump())
        if viewed is None:
            raise HTTPException(status_code=404, detail="film not found")
        return viewed
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
