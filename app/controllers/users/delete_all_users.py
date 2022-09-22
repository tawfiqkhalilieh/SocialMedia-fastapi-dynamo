from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException, Depends
from app.services.delete_all_users import delete_all_users as delete_all_users_crud
from app.models.constans import api_key_header
from app.services.create_user import create_user as create_user_crud
from app.services.get_user import get_user_role as get_user_role_crud
from app.models.User import User
import random
router = APIRouter()

@router.delete("/all", tags=["developer"])
def delete_all_users_(APIkey: str = Depends(api_key_header)):
    try:
        if get_user_role_crud(id=APIkey, username='tawfiq') in ["Modirator", "Modirator"]:
            delete_all_users_crud()
            create_user_crud(
                usr=User(id="0", name="tawfiq", username="tawfiq", email="tawfiq@Social.com", password="0", age=16,
                         gender="male", posts=[], banned=False, follows=[], followers=[], blocked=[],
                         bio="I am the CEO bitch", role="Modirator"))
            return random.randint(0,1)
        else:
            raise HTTPException(status_code=422)
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)