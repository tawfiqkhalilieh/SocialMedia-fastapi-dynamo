from app.config import settings
from app.database import dynamo as dynamodb
from botocore.exceptions import ClientError
from fastapi import HTTPException

def delete_all_users(responses=[]):
    try:
        table = dynamodb.get_resource().Table(settings.table)
        response = table.scan()
        scan = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            scan.extend(response['Items'])
        for index in scan:
            try:
                r = table.delete_item(Key={
                    "id": index["id"],
                    'username': index['username']
                })
                responses.append(r)
            except:
                responses.append((index["id"],None))
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)