# service/user_service.py
from typing import Dict, List

# Mock database for user profiles
user_profiles_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "john@example.com",
        "phone": "1234567890",
    }
}

def get_user_profile(username: str) -> Dict:
    if username in user_profiles_db:
        return user_profiles_db[username]
    return None

def update_user_profile(username: str, email: str, phone: str) -> Dict:
    if username in user_profiles_db:
        user_profiles_db[username]["email"] = email
        user_profiles_db[username]["phone"] = phone
        return user_profiles_db[username]
    return None

def get_repair_history(username: str) -> List[Dict]:
    # Mock repair history for the user
    return [
        {"order_id": 1, "description": "Leaking faucet", "status": "completed"},
        {"order_id": 2, "description": "Broken light", "status": "pending"},
    ]

def change_password(username: str, new_password: str) -> bool:
    if username in user_profiles_db:
        # In a real application, you would hash the new password here
        return True
    return False