from pydantic import BaseModel

class FilmCreateCommand(BaseModel):
    film_id: int
