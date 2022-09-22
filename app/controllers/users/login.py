from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException
from app.services.login import login as login_crud
router = APIRouter()
@router.post("/{username}/{password}", tags=["developer"])
def login(username:str,password:str):
    try:
        return(login_crud(username=username,password=password))
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)