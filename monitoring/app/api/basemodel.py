from pydantic import BaseModel
from typing import List

class Records(BaseModel):
    VAR1: int | None = None
    VAR2: int | None = None
    VAR3: float | None = None
    REF_DATE: int | None = None

class Records_list(BaseModel):
    records: List[Records]
