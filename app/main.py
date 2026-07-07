from fastapi import FastAPI
from app.api import router
print("ROUTER COUNT:", len(router.routes))

app = FastAPI(
    title="ARPI Enterprise",
    version="1.1.1-TEST",
    description="Advanced Risk Prediction Intelligence System"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "status": "online",
        "version": "1.1.1-TEST",
        "system": "ARPI Enterprise"
    }
