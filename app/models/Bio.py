from pydantic import BaseModel
class Bio(BaseModel):
    id: str
    username: str
    bio: str