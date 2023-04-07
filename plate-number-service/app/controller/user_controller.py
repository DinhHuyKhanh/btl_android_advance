from fastapi import APIRouter
from schemas import UserSchema
from app.settings import user_service
from app.settings import user_model

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/')
def get_all_user():
    return user_service.get_all_user(user_model)

@router.get('/{id}')
def get_user_by_id(id: int):
    return {'data': user_service.get_by_id(id, user_model)}

@router.post('')
async def create(user: UserSchema):
    user=user.dict()
    return {'data': user_service.create(user, user_model)}

@router.delete('/{id}')
async def delete(id: int):
    return {'code': user_service.delete_by_id(id, user_model)}