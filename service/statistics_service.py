# service/statistics_service.py
from typing import List, Dict

# Mock statistics data
repair_statistics_db = [
    {"repair_type": "plumbing", "count": 10, "average_duration": 2.5},
    {"repair_type": "electrical", "count": 5, "average_duration": 3.0},
]

def get_repair_statistics() -> List[Dict]:
    return repair_statistics_db