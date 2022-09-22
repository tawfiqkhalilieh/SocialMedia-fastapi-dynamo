from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException
from app.services.update_password import update_password as update_password_crud
from app.models.Bio import Bio as u
router = APIRouter()
@router.put('/bio', tags=["user"])
def update_password(usr : u):
    try:
        update_password_crud(usr)
    except ClientError as e:
        raise HTTPException(status_code=400,detail=e.response)