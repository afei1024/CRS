# api/statistics.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class RepairStatistic(BaseModel):
    repair_type: str
    count: int
    average_duration: float

# Mock statistics
repair_statistics_db = [
    {"repair_type": "plumbing", "count": 10, "average_duration": 2.5},
    {"repair_type": "electrical", "count": 5, "average_duration": 3.0},
]

# Get repair statistics
@router.get("/statistics", response_model=List[RepairStatistic])
async def get_repair_statistics():
    return repair_statistics_db