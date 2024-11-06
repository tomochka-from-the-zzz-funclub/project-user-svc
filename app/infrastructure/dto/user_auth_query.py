from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime

class UserAuthQuery(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, description="Пароль длиной не меньше 5 символов")