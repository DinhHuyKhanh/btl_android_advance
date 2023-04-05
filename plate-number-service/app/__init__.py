from fastapi import FastAPI
from app.router import api_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI()
    app.include_router(api_router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse({
                'code': -1,
                'message': f'Invalid params: {str(exc)}'
            }, status_code=200)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],)

    return app