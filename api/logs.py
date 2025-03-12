# api/logs.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class LogEntry(BaseModel):
    id: int
    action: str
    timestamp: str

# Mock database
logs_db = [
    {"id": 1, "action": "User logged in", "timestamp": "2023-10-01T12:00:00"},
    {"id": 2, "action": "Repair order submitted", "timestamp": "2023-10-01T12:05:00"},
]

# Get logs
@router.get("/operations", response_model=List[LogEntry])
async def get_logs():
    return logs_db