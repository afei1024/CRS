# service/notification_service.py
from typing import List, Dict

# Mock database for notifications
notifications_db = [
    {"id": 1, "message": "Repair order #1 has been assigned to you.", "is_read": False},
    {"id": 2, "message": "Repair order #2 status updated to 'In Progress'.", "is_read": True},
]

def get_notifications() -> List[Dict]:
    return notifications_db

def mark_notification_as_read(notification_id: int) -> Dict:
    for notification in notifications_db:
        if notification["id"] == notification_id:
            notification["is_read"] = True
            return notification
    return None