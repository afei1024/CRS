# api/feedback.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class Feedback(BaseModel):
    id: int
    message: str
    user: str

# Mock database
feedback_db = [
    {"id": 1, "message": "Great service!", "user": "johndoe"},
    {"id": 2, "message": "Need more repair types.", "user": "janedoe"},
]

# Get feedback
@router.get("/list", response_model=List[Feedback])
async def get_feedback():
    return feedback_db

# Submit feedback
@router.post("/submit")
async def submit_feedback(message: str, user: str):
    new_feedback = {"id": len(feedback_db) + 1, "message": message, "user": user}
    feedback_db.append(new_feedback)
    return {"message": "Feedback submitted successfully"}