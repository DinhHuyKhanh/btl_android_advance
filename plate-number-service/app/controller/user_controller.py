from fastapi import APIRouter
from util.helper import wrap_responses
from app.controller.schema import ResetPasswordSchema, UserLogin, UpdatePasswordSchema, UserSchema, UpdateUserSchema
from app.settings import UserModelImp, UserService

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.put('/forget_password')
@wrap_responses
async def reset_password(resetPassword: ResetPasswordSchema):
    resetPassword = resetPassword.dict()
    return UserService().reset_password(resetPassword, UserModelImp())

@router.get('/')
@wrap_responses
async def get_all_user():
    return UserService().get_all_user(UserModelImp())

@router.get('/{id}')
@wrap_responses
async def get_user_by_id(id: int):
    return UserService().get_by_id(id, UserModelImp())

@router.post('')
@wrap_responses
async def create(user: UserSchema):
    user=user.dict()
    return UserService().create(user, UserModelImp())

@router.delete('/{id}')
@wrap_responses
async def delete(id: int):
    return UserService().delete_by_id(id, UserModelImp())

@router.put('/{id}')
@wrap_responses
async def update(id: int, user: UpdateUserSchema):
    user = user.dict()
    return UserService().update(id, user, UserModelImp())

@router.put('/{id}/updatePassword')
@wrap_responses
async def update_password(id: int, update_password: UpdatePasswordSchema):
    update_password = update_password.dict()
    return UserService().update_password(id, update_password, UserModelImp())

@router.post('/login')
@wrap_responses
async def login(user: UserLogin):
    user_dict = user.dict()
    return UserService().login(user_dict, UserModelImp())
