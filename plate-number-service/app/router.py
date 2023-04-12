from fastapi import APIRouter
from app.controller.user_controller import router as user_router
from app.controller.detect_plate_controller import router as plate_router
from app.controller.email_controller import router as email_router
from app.controller.gate_history_controller import router as gate_history_router

api_router = APIRouter(
    prefix='/api/v1'
)

api_router.include_router(user_router)
api_router.include_router(plate_router)
api_router.include_router(email_router)
api_router.include_router(gate_history_router)
