from fastapi import APIRouter
from app.controller.schema import GateHistorySchema
from util.helper import wrap_responses
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