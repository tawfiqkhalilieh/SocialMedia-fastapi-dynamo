from botocore.exceptions import ClientError
from app.config import settings
from app.database import dynamo as dynamodb
from fastapi.exceptions import HTTPException
def get_user(id: str, username:str ):
    table = dynamodb.get_resource().Table(settings.table)
    try:
        return table.get_item(Key={'id': id, 'username': username})
    except ClientError:
        raise HTTPException(status_code=403,detail='User Not Found')

def get_user_role(id:str,username:str):
    table = dynamodb.get_resource().Table(settings.table)
    try:
        return table.get_item(Key={'id': id,'username':username})['Item']['role']
    except:
        raise HTTPException(status_code=404,detail='Authorization Failed')