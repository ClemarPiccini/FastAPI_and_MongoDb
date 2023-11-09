from fastapi import APIRouter

from model.user import user
from model.models import client

user = APIRouter()

@user.get('/user')
async def find_all_users():
    return client.local.user.find()