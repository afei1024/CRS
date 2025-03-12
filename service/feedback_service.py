# service/feedback_service.py
from typing import List, Dict

# Mock database for feedback
feedback_db = [
    {"id": 1, "message": "Great service!", "user": "johndoe"},
    {"id": 2, "message": "Need more repair types.", "user": "janedoe"},
]

def get_feedback() -> List[Dict]:
    return feedback_db

def submit_feedback(message: str, user: str) -> Dict:
    new_feedback = {"id": len(feedback_db) + 1, "message": message, "user": user}
    feedback_db.append(new_feedback)
    return new_feedback