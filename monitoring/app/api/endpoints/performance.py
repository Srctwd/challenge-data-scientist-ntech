"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter

router = APIRouter(prefix="/performance")

@router.get("")
def performance():
    return {"Hello performance"}


