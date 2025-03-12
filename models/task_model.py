# models/task_model.py
from pydantic import BaseModel

# 任务模型
class Task(BaseModel):
    id: int  # 任务ID
    order_id: int  # 关联的报修单ID
    technician: str  # 分配的维修人员
    status: str  # 任务状态（如：待处理、处理中、已完成）
    created_at: str  # 任务创建时间