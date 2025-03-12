# api/management.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class RepairOrder(BaseModel):
    order_id: int
    description: str
    images: List[str]
    repair_type: str
    status: str

# Mock database
repair_orders_db = [
    {
        "order_id": 1,
        "description": "Leaking faucet",
        "images": ["https://example.com/images/faucet.jpg"],
        "repair_type": "plumbing",
        "status": "pending",
    }
]

# Get all repair orders
@router.get("/list", response_model=List[RepairOrder])
async def get_repair_orders(status: str = None):
    if status:
        return [order for order in repair_orders_db if order["status"] == status]
    return repair_orders_db

# Get repair order details
@router.get("/detail/{order_id}", response_model=RepairOrder)
async def get_repair_order(order_id: int):
    for order in repair_orders_db:
        if order["order_id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# Assign repair order to technician
@router.post("/assign")
async def assign_repair_order(order_id: int, technician: str):
    for order in repair_orders_db:
        if order["order_id"] == order_id:
            order["technician"] = technician
            return {"message": "Order assigned successfully"}
    raise HTTPException(status_code=404, detail="Order not found")

# Update repair order status
@router.post("/update-status")
async def update_repair_order_status(order_id: int, status: str):
    for order in repair_orders_db:
        if order["order_id"] == order_id:
            order["status"] = status
            return {"message": "Order status updated successfully"}
    raise HTTPException(status_code=404, detail="Order not found")