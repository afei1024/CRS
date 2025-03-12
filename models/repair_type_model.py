# models/repair_type_model.py
from pydantic import BaseModel

# 维修类型模型
class RepairType(BaseModel):
    id: int  # 维修类型ID
    name: str  # 维修类型名称（如：水管、电路）