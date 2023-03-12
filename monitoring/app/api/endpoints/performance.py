#Endpoint for performance calculations.
from fastapi import APIRouter, Request

router = APIRouter(prefix="/performance")

@router.post("")
async def performance(records: Request):
    data = await records.json()
    return 21
