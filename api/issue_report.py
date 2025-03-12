# api/issue_report.py
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class RepairOrder(BaseModel):
    description: str
    images: List[str]
    repair_type: str

# Mock database
repair_orders_db = []

# Issue reporting endpoint
@router.post("/submit")
async def submit_repair(description: str, repair_type: str, images: List[UploadFile] = File(...)):
    image_urls = []
    for image in images:
        # Save image to server or cloud storage
        image_url = f"https://example.com/images/{image.filename}"
        image_urls.append(image_url)
    repair_order = {
        "description": description,
        "images": image_urls,
        "repair_type": repair_type,
        "order_id": len(repair_orders_db) + 1,
    }
    repair_orders_db.append(repair_order)
    return {"order_id": repair_order["order_id"]}