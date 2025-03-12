# service/technician_service.py
from typing import List, Dict

# Mock database for repair tasks
repair_tasks_db = [
    {
        "order_id": 1,
        "description": "Leaking faucet",
        "images": ["https://example.com/images/faucet.jpg"],
        "repair_type": "plumbing",
        "status": "assigned",
        "technician": "tech1",
    }
]

def get_technician_tasks(technician: str) -> List[Dict]:
    return [task for task in repair_tasks_db if task.get("technician") == technician]

def update_task_status(order_id: int, status: str) -> Dict:
    for task in repair_tasks_db:
        if task["order_id"] == order_id:
            task["status"] = status
            return task
    return None