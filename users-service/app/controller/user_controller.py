from fastapi import APIRouter
from app.controller.schema import UserSchema, UserUpdateSchema
from app.settings import user_service
from app.settings import user_model

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('')
def get_all_user():
    return {'data': user_service.get_all_user(user_model)}

@router.get('/{id}')
def get_user_by_id(id: int):
    return {'data': id}

@router.put("/{id}")
def update(id: int, user: UserUpdateSchema ):
    user=user.dict()
    return {'id': id, 'user': {'email': user["email"], 'full_name': user['full_name']}}

@router.post('')
async def create(user: UserSchema):
    user=user.dict()
    return user

@router.delete('/{id}')
async def delete(id: int):
    return {'id': id}
