from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime

class UserUpdateCommand(BaseModel):
    email: EmailStr | None = Field(None, description="Новая электронная почта")
    name: str | None = Field(None, description="Новое имя")
    surname: str | None = Field(None, description="Новая фамилия")
    birth: date | None = Field(None, description="Новая дата рождения в формате ГГГГ-ММ-ДД")

    @classmethod
    @field_validator("birth")
    def validate_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values
