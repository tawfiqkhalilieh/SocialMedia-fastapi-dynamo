from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException,Depends
from app.services.delete_user import delete_user as delete_user_crud
from app.models.constans import api_key_header
from app.services.get_user import get_user_role as get_user_role_crud
router = APIRouter()
@router.delete("/{id}/{username}", tags=["developer"])
def delete_user(id: str,username:str,apiKEY: str = Depends(api_key_header)):
    try:
        if get_user_role_crud(id=apiKEY, username=username) in ["Modirator", "Admin"]:
            return delete_user_crud(id=id, username=username)
        else:
            raise HTTPException(status_code=403)
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)