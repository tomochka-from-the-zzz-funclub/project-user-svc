from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime

class ChangePassCommand(BaseModel):
    password: str = Field(..., min_length=5, description="Новый пароль длиной не меньше 5 символов")
    code: str = Field(..., description="Код подтверждения")
