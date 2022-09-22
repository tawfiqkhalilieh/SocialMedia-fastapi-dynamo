from pydantic import BaseModel
class Comment(BaseModel):
    id: str # authors's ID
    comment_id:str # comment's ID
    username: str # authors's username
    content: str # the comment