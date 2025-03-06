# app/config/redis_config.py（参考‌:ml-citation{ref="1,3" data="citationList"}）
import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)
