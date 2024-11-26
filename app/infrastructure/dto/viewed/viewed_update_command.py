from pydantic import BaseModel
from datetime import time

class ViewedUpdateCommand(BaseModel):
    timecode: time
