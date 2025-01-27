from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime

class User(BaseModel):
    # model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, description="Пароль длиной не меньше 5 символов")
    name: str
    surname: str
    birth: date = Field(..., description="Дата рождения в формате ГГГГ-ММ-ДД")
    subscription: bool

    @classmethod
    @field_validator("birth")
    def validate_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values