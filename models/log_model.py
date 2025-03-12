# models/log_model.py
from pydantic import BaseModel

# 日志模型
class Log(BaseModel):
    id: int  # 日志ID
    action: str  # 操作描述（如：用户登录、报修提交）
    user_id: int  # 执行操作的用户ID
    timestamp: str  # 操作时间