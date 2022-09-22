from app.config import settings
from app.database import dynamo as dynamodb
from fastapi.exceptions import HTTPException
from botocore.exceptions import ClientError

def delete_user(id: str, username: str):
    try:
        table = dynamodb.get_resource().Table(settings.table)
        table.delete_item(
            Key={
                'id': id,
                'username': username,
            }
        )
    except ClientError as e:
        raise HTTPException(status_code=400,detail=e.detail)