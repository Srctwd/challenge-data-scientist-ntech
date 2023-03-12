#Endpoint for performance calculations.
from fastapi import APIRouter, Request
import pandas as pd

router = APIRouter(prefix="/performance")

@router.post("")
async def performance(records: Request):
    data = await records.json()
    df = pd.DataFrame(data)
    response = df["REF_DATE"].str[:7].value_counts().to_dict()
    
    return response
