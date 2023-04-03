from app.controller.schema import *
from fastapi import APIRouter
from app.settings import *

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get(
  '/',
  )
def get_all_user():
    return user_service.get_all_user(user_model)


@router.post('/login')
async def login(logInForm: LoginForm):
    try:
        data = logInForm.dict()
        return user_service.authenticate_user(data, user_model)
    except Exception as e:
        print("logIn " + str(e))

@router.post('/signup')
async def signUp(signUpForm: SignUpForm):
    try:
        data = signUpForm.dict()
        return user_service.create_user(data, user_model)
    except Exception as e:
        print("signup " + str(e))