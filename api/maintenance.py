# api/maintenance.py
from fastapi import APIRouter

router = APIRouter()

# Maintenance status
@router.get("/status")
async def get_maintenance_status():
    return {"status": "No maintenance scheduled"}