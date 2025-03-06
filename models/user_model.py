# app/models/user_model.py（参考‌:ml-citation{ref="2,5" data="citationList"}）
from sqlalchemy import Column, Integer, String
from app.config.db_config import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))  # 加密后的密码
