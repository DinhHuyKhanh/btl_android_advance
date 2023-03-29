import json
from fastapi import APIRouter, status
import requests
from app.controller.schema import UserSchema, UserUpdateSchema
from app.settings import user_service
import httpx


router = APIRouter(
    prefix='/users',
    tags=['users']
)

url = "http://localhost:8001/"

@router.get('')
async def get_all_user():
    response = requests.get(f"{url}api/v1/users/")
    return response.json()

@router.get('/{id}')
async def get_user_by_id(id: int):
    response = requests.get(f"{url}api/v1/users/{id}")
    return response.json()

@router.put('/{id}')
async def update(id: int, user: UserUpdateSchema):
    user=user.dict()
    response = requests.put(f"{url}api/v1/users/{id}", json=user)
    return response.json()

@router.post('')
async def create(user: UserSchema):
    user=user.dict()
    response = requests.post(f"{url}api/v1/users/", json=user)
    return response.json()

@router.delete('/{id}')
async def delete(id: int):
    response = requests.delete(f"{url}api/v1/users/{id}")
    return response.json()