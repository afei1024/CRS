# models/settings_model.py
from pydantic import BaseModel

# 系统设置模型
class SystemSettings(BaseModel):
    id: int  # 设置ID
    key: str  # 设置项名称（如：最大报修单数量）
    value: str  # 设置项值