from pydantic import BaseModel

class GenreCreateCommand(BaseModel):
    genre_id: int
