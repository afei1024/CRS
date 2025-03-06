from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 模拟学生数据库（实际需替换为数据库操作）
fake_students_db = {
    "student1": {"password": "student123", "name": "John Doe"},
    "student2": {"password": "student456", "name": "Jane Doe"}
}

# 模拟报修数据库（实际需替换为数据库操作）
fake_issues_db = []

class IssueReport(BaseModel):
    title: str
    description: str
    location: str

async def verify_student(username: str, password: str):
    """验证学生身份"""
    student = fake_students_db.get(username)
    if not student or student["password"] != password:
        return None
    return student

@app.get("/student_login", response_class=HTMLResponse)
async def student_login_page(request: Request):
    """渲染学生登录页面"""
    return templates.TemplateResponse("student_login.html", {"request": request})

@app.post("/student_login")
async def student_login_submit(
    request: Request,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    """处理学生登录请求"""
    student = await verify_student(username, password)
    if not student:
        return templates.TemplateResponse(
            "student_login.html",
            {"request": request, "error": "用户名或密码错误"},
            status_code=401
        )
    # 登录成功跳转至报修页面
    response = RedirectResponse(url="/report_issue", status_code=302)
    response.set_cookie(key="student_session", value=username)
    return response

@app.get("/report_issue", response_class=HTMLResponse)
async def report_issue_page(request: Request):
    """渲染报修页面"""
    return templates.TemplateResponse("report_issue.html", {"request": request})

@app.post("/report_issue")
async def report_issue_submit(
    request: Request,
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    location: Annotated[str, Form()]
):
    """处理报修请求"""
    student_session = request.cookies.get("student_session")
    if not student_session:
        raise HTTPException(status_code=401, detail="未登录")

    issue = IssueReport(title=title, description=description, location=location)
    fake_issues_db.append(issue.dict())

    return templates.TemplateResponse(
        "report_issue.html",
        {"request": request, "success": "报修成功"},
        status_code=200
    )

@app.get("/view_issues", response_class=HTMLResponse)
async def view_issues_page(request: Request):
    """查看所有报修问题"""
    student_session = request.cookies.get("student_session")
    if not student_session:
        raise HTTPException(status_code=401, detail="未登录")

    return templates.TemplateResponse(
        "view_issues.html",
        {"request": request, "issues": fake_issues_db}
    )
