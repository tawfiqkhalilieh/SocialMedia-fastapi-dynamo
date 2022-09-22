from app.config import settings
from app.database import dynamo as dynamodb
from app.models.update_password import Update_Password as u
from botocore.exceptions import ClientError
from fastapi import HTTPException

def update_password(usr: u):
    try:
        table = dynamodb.get_resource().Table(settings.table)
        response = table.update_item(
            Key={
                'id': usr.id,
                'username': usr.username,
            },
            UpdateExpression="set password = :r",
            ExpressionAttributeValues={
                ':r': usr.password,
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)