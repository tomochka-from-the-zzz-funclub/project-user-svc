from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.db.db import Base, int_pk
from datetime import time

class Viewed(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    film_id: Mapped[int]
    timecode: Mapped[time] = mapped_column(nullable=True)

    __table_args__ = (
        UniqueConstraint("user_id", "film_id", name="uq_user_film_viewed"),
    )
