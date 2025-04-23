from pydantic import BaseModel

class TaskRequest(BaseModel):
    param1: str
    param2: int = None