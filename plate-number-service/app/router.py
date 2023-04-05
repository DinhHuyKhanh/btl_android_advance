from fastapi import APIRouter
from app.controller.blog_get import router as blog_get_router
from app.controller.blog_post import router as blog_post_router
from app.controller.user_controller import router as user_router
from app.controller.detect_plate_controller import router as plate_router

api_router = APIRouter(
    prefix='/api/v1'
)

api_router.include_router(blog_get_router)
api_router.include_router(blog_post_router)
api_router.include_router(user_router)
api_router.include_router(plate_router)
