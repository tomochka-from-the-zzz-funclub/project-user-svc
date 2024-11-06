from sqlalchemy.orm import Mapped
from app.infrastructure.db.db import Base, str_uniq, int_pk
from datetime import date

class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    password: Mapped[str_uniq]
    name: Mapped[str]
    surname: Mapped[str]
    birth: Mapped[date]
    subscription: Mapped[bool]
    is_admin: Mapped[bool]

    # major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)
    # major: Mapped["Major"] = relationship("Major", back_populates="students")

    # def __str__(self):
    #     return (f"{self.__class__.__name__}(id={self.id}, "
    #             f"first_name={self.first_name!r},"
    #             f"last_name={self.last_name!r})")
    #
    # def __repr__(self):
    #     return str(self)