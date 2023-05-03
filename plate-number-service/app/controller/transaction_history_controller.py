from fastapi import APIRouter
from app.settings import TransactionHistoryImplement
from app.settings import TransactionService
from util.helper import wrap_responses


router = APIRouter(
    prefix='/transactions',
    tags=['transactions']
)

@router.get('')
@wrap_responses
async def get_all_by_user_id(user_id: int, data: str = None):
    return TransactionService().get_all_by_user_id(user_id, data, TransactionHistoryImplement())