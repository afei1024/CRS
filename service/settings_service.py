# service/settings_service.py
from typing import List, Dict

# Mock database for repair types
repair_types_db = [
    {"id": 1, "name": "Plumbing"},
    {"id": 2, "name": "Electrical"},
]

# Mock database for users
users_db = [
    {"id": 1, "username": "admin", "role": "admin"},
    {"id": 2, "username": "tech1", "role": "technician"},
]

# Mock database for roles
roles_db = [
    {"id": 1, "name": "admin"},
    {"id": 2, "name": "technician"},
]

def get_repair_types() -> List[Dict]:
    return repair_types_db

def add_repair_type(name: str) -> Dict:
    new_repair_type = {"id": len(repair_types_db) + 1, "name": name}
    repair_types_db.append(new_repair_type)
    return new_repair_type

def get_users() -> List[Dict]:
    return users_db

def add_user(username: str, role: str) -> Dict:
    new_user = {"id": len(users_db) + 1, "username": username, "role": role}
    users_db.append(new_user)
    return new_user

def get_roles() -> List[Dict]:
    return roles_db

def add_role(name: str) -> Dict:
    new_role = {"id": len(roles_db) + 1, "name": name}
    roles_db.append(new_role)
    return new_role