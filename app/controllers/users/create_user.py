from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException , Body
from app.models.User import User
from app.services.create_user import create_user as create_user_crud
router = APIRouter()

create_user_example = {
  "name": "Tester Tester",
  "username": "tester.tester",
  "email": "tester@testingteam.com",
  "password": "Te$sster.!@#$%^&*",
  "age": 18,
  "gender": "male",
  "posts": [
    {
      "main": [
        "https://www.startuphub.ai/wp-content/uploads/altooro.jpg"
      ],
      "mentions": [
        "1",
        "2",
        "5"
      ],
      "comments": [
        {
          "id": "*",
          "comment_id": "1",
          "username": "tester.tester",
          "content": "I am commenting to my post lmao"
        }
      ],
      "likes": 5,
      "views": 10,
      "time": "12:12",
      "public": True
    }
  ],
  "banned": False,
  "follows": ["2","1","6"],
  "followers": ["2","1"],
  "blocked": ["77"],
  "bio": "It's the tester's bio (:",
  "role": "Modirator"
}
create_user_default = {
  "id": "string",
  "name": "string",
  "username": "string",
  "email": "user@example.com",
  "password": "string",
  "age": 0,
  "gender": "male",
  "banned": False,
  "follows": [],
  "followers": [],
  "blocked": [],
  "bio": "string",
  'role': 'User'
}
@router.post("/create/user", tags=["developer"])
def create_user(usr: User = Body(default=create_user_default,example=create_user_example)):
  try:
      return create_user_crud(usr=usr)
  except ClientError as e:
      raise HTTPException(status_code=400, detail=e.response)