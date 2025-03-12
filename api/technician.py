# api/technician.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class RepairTask(BaseModel):
    order_id: int
    description: str
    images: List[str]
    repair_type: str
    status: str

# Mock database
repair_tasks_db = [
    {
        "order_id": 1,
        "description": "Leaking faucet",
        "images": ["https://example.com/images/faucet.jpg"],
        "repair_type": "plumbing",
        "status": "assigned",
    }
]

# Get technician tasks
@router.get("/tasks", response_model=List[RepairTask])
async def get_technician_tasks(technician: str):
    return [task for task in repair_tasks_db if task.get("technician") == technician]

# Update task status
@router.post("/update-task-status")
async def update_task_status(order_id: int, status: str):
    for task in repair_tasks_db:
        if task["order_id"] == order_id:
            task["status"] = status
            return {"message": "Task status updated successfully"}
    raise HTTPException(status_code=404, detail="Task not found")