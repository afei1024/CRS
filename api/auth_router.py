# app/api/auth_router.py（参考‌:ml-citation{ref="5,6" data="citationList"}）
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from service.auth_service import authenticate_user
from config.redis_config import redis_client

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("student_login.html", {"request": request})

@router.post("/login")
async def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    user = await authenticate_user(username, password)
    if not user:
        return templates.TemplateResponse(
            "student_login.html",
            {"request": request, "error": "用户名或密码错误"},
            status_code=401
        )
    # 生成 JWT 并存储到 Redis（参考‌:ml-citation{ref="5" data="citationList"}）
    from app.utils.security import create_access_token
    token = create_access_token(data={"sub": username})
    redis_client.set(f"user_token:{username}", token, ex=3600)  # 缓存 1 小时
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie(key="access_token", value=token, httponly=True)
    return response
