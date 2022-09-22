from pydantic import BaseModel, validator, Extra,AnyUrl
from typing import Optional,List
from fastapi.exceptions import HTTPException
from app.models.comments import Comment
class Post(BaseModel, extra=Extra.forbid):
    main: List[AnyUrl] # photos / videos
    mentions: Optional[List[str]] # this list should contains tha mentioned id's
    comments: Optional[List[Comment]] # the list of the comments
    likes: int = 0
    views: int = 0
    time: str # I will Update this to date or hour soon
    public: bool = True
    @validator('main')
    def files_validate(cls, main):
        if not main:
            raise HTTPException(status_code=422,detail="missing photos or videos")
        return main