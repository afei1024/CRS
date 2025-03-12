# models/statistics_model.py
from pydantic import BaseModel

# 统计模型
class RepairStatistic(BaseModel):
    repair_type: str  # 维修类型
    count: int  # 报修单数量
    average_duration: float  # 平均处理时长（小时）