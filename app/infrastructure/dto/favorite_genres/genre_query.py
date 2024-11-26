from pydantic import BaseModel

class GenreQuery(BaseModel):
    genre_id: int

    # class Config:
    #     orm_mode = True
