# api/documentation.py
from fastapi import APIRouter

router = APIRouter()

# Documentation endpoint
@router.get("/docs")
async def get_documentation():
    return {"message": "Documentation is available at /docs"}