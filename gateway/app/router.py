from fastapi import APIRouter
from app.controller.user_controller import router as user_router

api_router = APIRouter(
    prefix='/api/v1'
)


api_router.include_router(user_router)
