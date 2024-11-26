from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.db.db import Base, int_pk

class FavoriteGenre(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    genre_id: Mapped[int]

    __table_args__ = (
        UniqueConstraint("user_id", "genre_id", name="uq_user_genre"),
    )
