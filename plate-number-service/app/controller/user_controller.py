from fastapi import APIRouter
from util.helper import wrap_responses
from app.controller.schema import UserLogin, UserRegister
from app.settings import UserModelImp, UserModelImp, UserService

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('')
def get_all_user():
    return UserService().get_all_user(UserModelImp())

@router.post('')
@wrap_responses
async def create_user(user: UserRegister):
    user_dict = user.dict()
    return UserService().register(user_dict, UserModelImp())

@router.post('/login')
@wrap_responses
async def login(user: UserLogin):
    user_dict = user.dict()
    return UserService().login(user_dict, UserModelImp())
    