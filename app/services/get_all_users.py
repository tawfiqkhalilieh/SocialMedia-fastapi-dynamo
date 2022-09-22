from app.config import settings
from app.database import dynamo as dynamodb
from botocore.exceptions import ClientError
from fastapi import HTTPException

def get_all_users():
    try:
        table = dynamodb.get_resource().Table(settings.table)
        response = table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return data
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)