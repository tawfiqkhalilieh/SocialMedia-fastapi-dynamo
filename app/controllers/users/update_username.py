from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException,Depends
from app.services.get_user import get_user as get_user_crud
from app.services.delete_user import delete_user as delete_user_crud
from app.services.get_user import get_user_role as get_user_role_crud
from app.config import settings
from app.models.update_username import Update_Username as u
from app.database import dynamo as dynamodb
from app.models.constans import api_key_header
router = APIRouter()
@router.put("/username", tags=["developer"])
def update_username(user: u,apiKEY: str = Depends(api_key_header)):
    table = dynamodb.get_resource().Table(settings.table)
    try:
        if apiKEY != user.id:
            raise HTTPException(status_code=422)
        if get_user_role_crud(id=user.id, username=user.username) in ["Modirator", "Admin","User"]:
            usr = get_user_crud(id=user.id,username=user.username)
            delete_user_crud(id=user.id,username=user.username)
            usr["Item"]["username"] = user.newusername
            usr = usr["Item"]
            table.put_item(Item={**usr})
            return usr
        else:
            raise HTTPException(status_code=403)
    except ClientError as e:
        raise HTTPException(status_code=400,detail=e.response)