from app.config import settings
from app.database import dynamo as dynamodb
from botocore.exceptions import ClientError
from fastapi import HTTPException
def login(username: str, password: str):
    try:
        table = dynamodb.get_resource().Table(settings.table)
        response = table.scan()
        users = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            users.extend(response['Items'])
        for user in users:
            if user["username"] == username:
                if user["password"] == password:
                    return user
                else:
                    raise HTTPException(status_code=403,detail='Incorrect username or password')
        raise HTTPException(status_code=403,detail='Incorrect username or password')
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)