from fastapi import APIRouter, HTTPException, Response, status
from app.settings import QrCodeService
from app.settings import UserImplement

router = APIRouter(
    prefix='/qrcode',
    tags=['qrcode']
)

@router.get('',
            responses = {
                200: {
                    "content": {"image/png": {}}
                },
                404: {
                    "content": {"application/json": {}}
                }
            },
            response_class=Response)
async def get_qrcode(id: int):
    binary_qrcode = QrCodeService().create_qrcode(id, UserImplement())

    if binary_qrcode:
        return Response(content=binary_qrcode, media_type="image/png")
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="can't get qrcode"
    )
