from pydantic import BaseModel
class Update_Followers(BaseModel):
    id: str
    username:str
    follower_id: str