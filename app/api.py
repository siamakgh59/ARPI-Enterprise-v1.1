from fastapi import APIRouter
from app.market import market_snapshot

router = APIRouter()


@router.get("/market")
def market():
    return market_snapshot()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "engine": "ARPI Enterprise"
    }
