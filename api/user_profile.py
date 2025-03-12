# api/user_profile.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Models
class UserProfile(BaseModel):
    username: str
    email: str
    phone: str

# Mock user database
user_profiles_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "john@example.com",
        "phone": "1234567890",
    }
}

# Get user profile
@router.get("/profile", response_model=UserProfile)
async def get_user_profile(username: str):
    if username in user_profiles_db:
        return user_profiles_db[username]
    raise HTTPException(status_code=404, detail="User not found")

# Update user profile
@router.post("/update-profile")
async def update_user_profile(username: str, email: str, phone: str):
    if username in user_profiles_db:
        user_profiles_db[username]["email"] = email
        user_profiles_db[username]["phone"] = phone
        return {"message": "Profile updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")