from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException , Depends
from app.services.update_password import update_password as update_password_crud
from app.services.get_user import get_user_role as get_user_role_crud
from app.models.update_password import Update_Password as u
from app.models.constans import api_key_header
router = APIRouter()
@router.put('/password', tags=["developer"])
def update_password(usr : u,apiKEY: str = Depends(api_key_header)):
    try:
        if get_user_role_crud(id=apiKEY, username=usr.username) in ["Modirator", "Admin","User"]:
            update_password_crud(usr)
        else:
            raise HTTPException(status_code=403)
    except ClientError as e:
        raise HTTPException(status_code=400,detail=e.response)