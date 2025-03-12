# api/testing.py
from fastapi import APIRouter

router = APIRouter()

# Test endpoint
@router.get("/test")
async def test_endpoint():
    return {"message": "Test endpoint is working"}