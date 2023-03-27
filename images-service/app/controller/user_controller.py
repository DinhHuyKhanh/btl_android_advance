from fastapi import APIRouter, Response, status
from enum import Enum
from typing import Optional
from app.service.user_service import UserService
from app.settings import user_service
from app.settings import user_model

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get(
  '/',
  )
def get_all_user():
    return user_service.get_all_user(user_model)