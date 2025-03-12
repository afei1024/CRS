# service/repair_service.py
from typing import List, Dict

# Mock database for repair orders
repair_orders_db = []

def submit_repair(description: str, repair_type: str, images: List[str]) -> Dict:
    repair_order = {
        "description": description,
        "images": images,
        "repair_type": repair_type,
        "order_id": len(repair_orders_db) + 1,
        "status": "pending",
    }
    repair_orders_db.append(repair_order)
    return repair_order

def get_repair_orders(status: str = None) -> List[Dict]:
    if status:
        return [order for order in repair_orders_db if order["status"] == status]
    return repair_orders_db

def get_repair_order(order_id: int) -> Dict:
    for order in repair_orders_db:
        if order["order_id"] == order_id:
            return order
    return None

def assign_repair_order(order_id: int, technician: str) -> Dict:
    for order in repair_orders_db:
        if order["order_id"] == order_id:
            order["technician"] = technician
            return order
    return None

def update_repair_order_status(order_id: int, status: str) -> Dict:
    for order in repair_orders_db:
        if order["order_id"] == order_id:
            order["status"] = status
            return order
    return None