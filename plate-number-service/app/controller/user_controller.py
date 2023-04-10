from fastapi import APIRouter
from util.helper import wrap_responses
from schemas import ResetPasswordSchema, UpdatePasswordSchema, UserSchema, UpdateUserSchema
from app.settings import user_service
from app.settings import user_model

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.put('/forget_password')
@wrap_responses
async def reset_password(resetPassword: ResetPasswordSchema):
    resetPassword = resetPassword.dict()
    return user_service.reset_password(resetPassword, user_model)

@router.get('/')
@wrap_responses
async def get_all_user():
    return user_service.get_all_user(user_model)

@router.get('/{id}')
@wrap_responses
async def get_user_by_id(id: int):
    return user_service.get_by_id(id, user_model)

@router.post('')
@wrap_responses
async def create(user: UserSchema):
    user=user.dict()
    return user_service.create(user, user_model)

@router.delete('/{id}')
@wrap_responses
async def delete(id: int):
    return user_service.delete_by_id(id, user_model)

@router.put('/{id}')
@wrap_responses
async def update(id: int, user: UpdateUserSchema):
    user = user.dict()
    return user_service.update(id, user, user_model)

@router.put('/{id}/updatePassword')
@wrap_responses
async def update_password(id: int, update_password: UpdatePasswordSchema):
    update_password = update_password.dict()
    return user_service.update_password(id, update_password, user_model)
