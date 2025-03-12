# models/repair_model.py
from pydantic import BaseModel
from typing import List, Optional

# 报修单模型
class RepairOrder(BaseModel):
    id: int  # 报修单ID
    description: str  # 问题描述
    images: List[str]  # 图片URL列表
    repair_type: str  # 维修类型（如：水管、电路）
    status: str  # 报修单状态（如：待处理、处理中、已完成）
    user_id: int  # 提交报修的用户ID
    technician: Optional[str] = None  # 分配的维修人员（可选）
    created_at: str  # 报修单创建时间

# 报修单提交模型
class RepairSubmit(BaseModel):
    description: str  # 问题描述
    images: List[str]  # 图片URL列表
    repair_type: str  # 维修类型

# 报修单更新模型
class RepairUpdate(BaseModel):
    status: Optional[str] = None  # 报修单状态（可选）
    technician: Optional[str] = None  # 分配的维修人员（可选）