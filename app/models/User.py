from app.models.Gender import Gender
from pydantic import  BaseModel,EmailStr,validator
from typing import Optional,List
from app.models.post import Post
from fastapi.exceptions import HTTPException
from app.models.Roles import Roles
import re
class User(BaseModel):
    id: Optional[str] # id for testers and VIP users
    name: str # user's full name
    username: str # user's username
    email:EmailStr # user's email
    password: str # user's password
    age: int # user's age
    gender: Gender # user's gender
    posts: Optional[List[Post]] # list of the user's posts
    banned: bool = False
    follows: List[str] = [] # this list should contains the id's of the users this user follow
    followers: List[str] = [] # this list should contains the id's of the users of user's followers
    blocked: List[str] = [] # this list should contains the id's of the users this user block
    bio: str = ""
    role: Roles = "User"

    @validator('age') # here I block creating the account for young users
    def age_validator(cls, age):
        if age<13:
            try:
                raise HTTPException(status_code=422)
            except:
                pass
        return age

    @validator('banned') # simply you can't create banned user
    def ban_validation(cls,banned):
        if not banned:
            try:
                raise HTTPException(status_code=422)
            except:
                pass
        return banned

    @validator('bio')
    def bio_validator(cls,bio):
        if len(bio)>150:
            try:
                raise HTTPException(status_code=422)
            except:
                pass
        return bio

    @validator('password')
    def passwords_validator(cls, v, values, **kwargs):
        if 'role' in values and values['role'] == 'User' and len(v) < 8 and (not re.search("[a-z]", v) or not re.search("[A-Z]", v) or not re.search("[0-9]", v) or not re.search("[_*^#@$]", v) or re.search("\s", v)):
            try:
                raise HTTPException(status_code=422)
            except:
                pass
        return v