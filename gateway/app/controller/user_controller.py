from fastapi import APIRouter
import requests
from app.controller.schema import UserSchema, UserUpdateSchema
from conf import USER_SERVICE_URL


router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('')
async def get_all_user():
    response = requests.get(f"{USER_SERVICE_URL}")
    return response.json()

@router.get('/{id}')
async def get_user_by_id(id: int):
    response = requests.get(f"{USER_SERVICE_URL}/{id}")
    return response.json()

@router.put('/{id}')
async def update(id: int, user: UserUpdateSchema):
    user=user.dict()
    response = requests.put(f"{USER_SERVICE_URL}/{id}", json=user)
    return response.json()

@router.post('')
async def create(user: UserSchema):
    user=user.dict()
    response = requests.post(f"{USER_SERVICE_URL}/", json=user)
    return response.json()

@router.delete('/{id}')
async def delete(id: int):
    response = requests.delete(f"{USER_SERVICE_URL}/{id}")
    return response.json()