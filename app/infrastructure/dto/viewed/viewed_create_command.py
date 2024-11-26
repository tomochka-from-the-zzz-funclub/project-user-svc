from pydantic import BaseModel

class ViewedCreateCommand(BaseModel):
    film_id: int
