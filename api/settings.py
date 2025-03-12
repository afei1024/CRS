# api/settings.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Models
class RepairType(BaseModel):
    id: int
    name: str

class User(BaseModel):
    id: int
    username: str
    role: str

class Role(BaseModel):
    id: int
    name: str

# Mock database
repair_types_db = [
    {"id": 1, "name": "Plumbing"},
    {"id": 2, "name": "Electrical"},
]

users_db = [
    {"id": 1, "username": "admin", "role": "admin"},
    {"id": 2, "username": "tech1", "role": "technician"},
]

roles_db = [
    {"id": 1, "name": "admin"},
    {"id": 2, "name": "technician"},
]

# Repair type management
@router.get("/repair-types", response_model=List[RepairType])
async def get_repair_types():
    return repair_types_db

@router.post("/repair-types")
async def add_repair_type(name: str):
    new_repair_type = {"id": len(repair_types_db) + 1, "name": name}
    repair_types_db.append(new_repair_type)
    return {"message": "Repair type added successfully"}

# User management
@router.get("/users", response_model=List[User])
async def get_users():
    return users_db

@router.post("/users")
async def add_user(username: str, role: str):
    new_user = {"id": len(users_db) + 1, "username": username, "role": role}
    users_db.append(new_user)
    return {"message": "User added successfully"}

# Role management
@router.get("/roles", response_model=List[Role])
async def get_roles():
    return roles_db

@router.post("/roles")
async def add_role(name: str):
    new_role = {"id": len(roles_db) + 1, "name": name}
    roles_db.append(new_role)
    return {"message": "Role added successfully"}