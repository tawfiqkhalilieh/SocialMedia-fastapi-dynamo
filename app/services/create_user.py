from botocore.exceptions import ClientError
from fastapi import HTTPException
from app.database import dynamo as dynamodb
from app.models.User import User
from app.config import settings
from app.services.get_all_users import get_all_users
import uuid
def create_user(usr: User):
    if not usr.id:
        id = str(uuid.uuid4())
    else:
        id = usr.id
    try:
        table = dynamodb.get_resource().Table(settings.table)
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)
    try:
        users = get_all_users()
        for userr in users:
            if not userr["banned"] and userr["username"] == usr.username:
                raise HTTPException(status_code=422,detail='this username is already taken')
            if not userr["banned"] and userr["email"] == usr.username:
                raise HTTPException(status_code=422,detail='this email is already taken')
        table.put_item(Item={**usr.dict(),'id': id})
    except ClientError:
        table.put_item(Item={'id': id, **usr.dict(),'id': id})
    return {**usr.dict(),'id': id}