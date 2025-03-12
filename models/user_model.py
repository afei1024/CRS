# models/user_model.py
from pydantic import BaseModel
from typing import Optional

# 用户模型
class User(BaseModel):
    id: int  # 用户ID
    username: str  # 用户名
    email: Optional[str] = None  # 邮箱（可选）
    phone: Optional[str] = None  # 手机号（可选）
    role: str  # 用户角色（如：学生、管理员、维修人员）
    hashed_password: str  # 加密后的密码

# 用户登录模型
class UserLogin(BaseModel):
    username: str  # 用户名
    password: str  # 密码

# 用户注册模型
class UserRegister(BaseModel):
    username: str  # 用户名
    email: str  # 邮箱
    phone: str  # 手机号
    password: str  # 密码
    role: str  # 用户角色

# 用户更新模型
class UserUpdate(BaseModel):
    email: Optional[str] = None  # 邮箱（可选）
    phone: Optional[str] = None  # 手机号（可选）# app/models/user_model.py（参考‌:ml-citation{ref="2,5" data="citationList"}）
