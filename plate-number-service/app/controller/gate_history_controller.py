from fastapi import APIRouter
from app.controller.schema import GateHistorySchema
from util.helper import wrap_list_responses, wrap_responses
from app.settings import GateHistoryImplement, GateService

router = APIRouter(
    prefix='/gate_histories',
    tags=['gate_histories']
)

@router.get('')
@wrap_responses
async def get_all_gate_histories(id: int):
    return GateService().get_all_gate_histories(id, GateHistoryImplement())

@router.post('')
@wrap_responses
async def create(data: GateHistorySchema):
    data = data.dict()
    return GateService().create(data, GateHistoryImplement())

@router.get('/all/')
@wrap_list_responses
async def get_all(limit: int = 20, offset: int = 0, sort: str ='asc', start_date = None , end_date = None):
    return GateService().get_all(limit, offset, sort, start_date, end_date,GateHistoryImplement())
