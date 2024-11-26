from pydantic import BaseModel
from datetime import time

class ViewedQuery(BaseModel):
    film_id: int
    timecode: time | None
