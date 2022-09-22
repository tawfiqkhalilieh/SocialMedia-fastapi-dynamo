from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException
from app.services.get_user import get_user as get_user_crud
router = APIRouter()

@router.get("/{id}/{username}", tags=["developer"])
def get_user(id: str,username: str):
    try:
        try:
            return get_user_crud(id=id,username=username)['Item']
        except:
            raise HTTPException(status_code=400, detail='user not found')
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)
