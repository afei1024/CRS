# api/support.py
from fastapi import APIRouter

router = APIRouter()

# Support status
@router.get("/status")
async def get_support_status():
    return {"status": "Support is available"}