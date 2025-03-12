# service/logs_service.py
from typing import List, Dict

# Mock database for logs
logs_db = [
    {"id": 1, "action": "User logged in", "timestamp": "2023-10-01T12:00:00"},
    {"id": 2, "action": "Repair order submitted", "timestamp": "2023-10-01T12:05:00"},
]

def get_logs() -> List[Dict]:
    return logs_db