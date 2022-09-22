from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends, HTTPException
from app.services.get_user import get_user_role as get_user_role_crud
from app.services.get_all_users import get_all_users as get_all_users_crud
from app.models.constans import api_key_header
router = APIRouter()

@router.get("/all/u/{username}", tags=["developer"])
def getallusers(username:str , apiKEY: str = Depends(api_key_header)):
    try:
        if get_user_role_crud(id=apiKEY, username=username) not in ["Modirator", "Modirator"]:
            raise HTTPException(status_code=403)
        return get_all_users_crud()
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)