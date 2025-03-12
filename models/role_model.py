# models/role_model.py
from pydantic import BaseModel

# 角色模型
class Role(BaseModel):
    id: int  # 角色ID
    name: str  # 角色名称（如：管理员、维修人员）