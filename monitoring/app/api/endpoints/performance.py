"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter
from api.basemodel import Records_list

router = APIRouter(prefix="/performance")

#@router.get("")
#def performance():
#    return {"Hello performance"}

@router.post("")
async def performance(records: Records_list):
    return records

print(Records_list.__fields__)
#print(Records_list.parse_raw('{"VAR1":1},{"VAR1":1}'))
