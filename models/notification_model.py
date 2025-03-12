# models/notification_model.py
from pydantic import BaseModel

# 通知模型
class Notification(BaseModel):
    id: int  # 通知ID
    message: str  # 通知内容
    user_id: int  # 接收通知的用户ID
    is_read: bool  # 是否已读
    created_at: str  # 通知创建时间
