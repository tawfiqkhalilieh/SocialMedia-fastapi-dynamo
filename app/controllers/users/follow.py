from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException,Depends
from app.services.update_followers import add_follower as add_follower_crud
from app.services.get_user import get_user_role as get_user_role_crud
from app.models.update_followers import Update_Followers as u
from app.models.constans import api_key_header
router = APIRouter()
@router.put("/follow", tags=["user"])
def follow(usr: u,apiKEY: str = Depends(api_key_header)):
    try:
        try:
            if get_user_role_crud(id=apiKEY,username=usr.username) in ["Modirator","Admin","User"]:
                return add_follower_crud(usr)
        except:
            raise HTTPException(status_code=422)
    except ClientError as e:
        raise HTTPException(status_code=400,detail=e.response)