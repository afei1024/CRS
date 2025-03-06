# app/service/auth_service.py（参考‌:ml-citation{ref="5,7" data="citationList"}）
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.config.db_config import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def authenticate_user(username: str, password: str):
    db = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user
