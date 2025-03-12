# api/notification.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class Notification(BaseModel):
    id: int
    message: str
    is_read: bool

# Mock database
notifications_db = [
    {"id": 1, "message": "Repair order #1 has been assigned to you.", "is_read": False},
    {"id": 2, "message": "Repair order #2 status updated to 'In Progress'.", "is_read": True},
]

# Get notifications
@router.get("/list", response_model=List[Notification])
async def get_notifications():
    return notifications_db

# Mark notification as read
@router.post("/mark-as-read")
async def mark_as_read(notification_id: int):
    for notification in notifications_db:
        if notification["id"] == notification_id:
            notification["is_read"] = True
            return {"message": "Notification marked as read"}
    raise HTTPException(status_code=404, detail="Notification not found")