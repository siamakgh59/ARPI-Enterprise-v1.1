from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="ARPI Enterprise",
    version="1.1.1-TEST",
    description="Advanced Risk Prediction Intelligence System"
)

app.include_router(router)

app.include_router(router)


@app.get("/")
def root():
    return {
        "project": "ARPI",
        "version": "1.1.0",
        "status": "running"
    }
