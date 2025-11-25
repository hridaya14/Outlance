from fastapi import APIRouter


router = APIRouter()


@router.get("/ping", tags=["Health"])
async def ping():
    """Simple ping endpoint for basic connectivity tests."""
    return {"status": "ok", "message": "pong"}


@router.get("/health", tags=["Health"])
async def ping():
    """Health Check endpoint for the status of the api"""
    return {"status": "ok"}
