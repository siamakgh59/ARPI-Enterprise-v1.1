from fastapi import APIRouter
from app.market import market_snapshot

router = APIRouter()


@router.get("/market")
def market():
    return market_snapshot()


@router.get("/market/live")
def market_live():
    return {
        "engine": "ARPI Live Market Engine",
        "status": "LIVE",
        "data": market_snapshot()
    }


@router.get("/health")
def health():
    return {
        "status": "ok",
        "engine": "ARPI Enterprise"
    }
