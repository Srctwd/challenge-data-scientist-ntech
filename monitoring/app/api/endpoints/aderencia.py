"""Endpoint para cálculo de aderência."""
from fastapi import APIRouter

router = APIRouter(prefix="/aderencia")

@router.get("")
def performance():
    return {"Hello aderencia"}


