from pydantic import BaseModel

class FilmQuery(BaseModel):
    film_id: int

    # class Config:
    #     orm_mode = True
