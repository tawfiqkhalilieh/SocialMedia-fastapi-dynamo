from app.config import settings
from app.database import dynamo as dynamodb
from app.models import Bio
from botocore.exceptions import ClientError
from fastapi import HTTPException

def update_password(usr: Bio):
    try:
        table = dynamodb.get_resource().Table(settings.table)
        response = table.update_item(
            Key={
                'id': usr.id,
                'username': usr.username,
            },
            UpdateExpression="set bio = :r",
            ExpressionAttributeValues={
                ':r': usr.bio,
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)