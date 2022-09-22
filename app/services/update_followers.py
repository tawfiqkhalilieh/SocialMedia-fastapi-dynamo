from app.config import settings
from app.database import dynamo as dynamodb
from app.models.update_followers import Update_Followers as u
from botocore.exceptions import ClientError
from fastapi import HTTPException

def add_follower(usr: u):
    try:
        if usr.id == usr.follower_id:
            raise HTTPException(status_code=403,detail="the user cann't follow him self")
        table = dynamodb.get_resource().Table(settings.table)
        followers_list = table.get_item(Key={'id': usr.id, 'username': usr.username})['Item']['followers']
        if not usr.follower_id in followers_list:
            followers_list.append(usr.follower_id)
        else:
            raise HTTPException(status_code=403, detail='the user is already following this user')
        response = table.update_item(
            Key={
                'id': usr.id,
                'username': usr.username,
            },
            UpdateExpression="set followers = :r",
            ExpressionAttributeValues={
                ':r': followers_list,
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)

def reomve_follower(usr: u):
    try:
        table = dynamodb.get_resource().Table(settings.table)
        followers_list = table.get_item(Key={'id': usr.id, 'username': usr.username})['Item']['followers']
        if usr.follower_id in followers_list:
            followers_list.remove(usr.follower_id)
        else:
            raise HTTPException(status_code=403,detail='you not following this user')
        response = table.update_item(
            Key={
                'id': usr.id,
                'username': usr.username,
            },
            UpdateExpression="set followers = :r",
            ExpressionAttributeValues={
                ':r': followers_list,
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        raise HTTPException(status_code=400, detail=e.response)