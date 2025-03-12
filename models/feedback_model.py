# models/feedback_model.py
from pydantic import BaseModel

# 反馈模型
class Feedback(BaseModel):
    id: int  # 反馈ID
    message: str  # 反馈内容
    user_id: int  # 提交反馈的用户ID
    created_at: str  # 反馈创建时间