import importlib
import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.routing import APIRoute
from core.root_logger import get_logger

logger = get_logger()

@asynccontextmanager  # 用于将一个异步函数转换为异步上下文管理器。它的核心作用是管理异步资源的生命周期，确保资源在使用完毕后能够被正确释放。
async def lifespan_fn(_: FastAPI) -> AsyncGenerator[None, None]:
    """
    lifespan_fn controls the startup and shutdown of the FastAPI Application.
    This function is called when the FastAPI application starts and stops.

    See FastAPI documentation for more information:
      - https://fastapi.tiangolo.com/advanced/events/
    """
    logger.info("start: 数据库初始化")

    logger.info("end: 数据初始化结束")

    # await start_scheduler()

    logger.info("-----SYSTEM STARTUP-----")
    logger.info("-----系统启动-----")
    logger.info("------APP SETTINGS------")
    logger.info("------应用程序设置------")
    # logger.info(
    #     settings.model_dump_json(
    #         indent=4,
    #         exclude={
    #             "SECRET",
    #             "SESSION_SECRET",
    #             "DB_URL",  # replace by DB_URL_PUBLIC for logs
    #             "DB_PROVIDER",
    #         },
    #     )
    # )
    logger.info("------APP FEATURES------")
    # logger.info("--------==SMTP==--------")
    # logger.info(settings.SMTP_FEATURE)
    # logger.info("--------==LDAP==--------")
    # logger.info(settings.LDAP_FEATURE)
    # logger.info("--------==OIDC==--------")
    # logger.info(settings.OIDC_FEATURE)
    # logger.info("-------==OPENAI==-------")
    # logger.info(settings.OPENAI_FEATURE)
    logger.info("------------------------")

    yield

    logger.info("-----SYSTEM SHUTDOWN----- \n")
    logger.info("-----系统关闭----- \n")

# <<<<<<  这个位置后续要调整成为可配置文件

# 系统描述
description = "这事一个校园报修系统，作为离开开发两年的练习项目"
# 版本号
APP_VERSION = "1.0.0"
# DOCS_URL
# REDOC_URL
# >>>>>>

app = FastAPI(
    title="校园报修系统",
    description=description,
    version=APP_VERSION,
    # docs_url=,  # 文档链接
    # redoc_url=REDOC_URL,
    lifespan=lifespan_fn,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:9001"],  # 替换为前端实际域名
    allow_credentials=True,
    allow_methods=["*"],  # 包含OPTIONS、POST等必要方法
    allow_headers=["*"],
)
# 自动注册所有路由
# Function to dynamically import and include routers
def include_routers():
    api_dir = "api"
    for module_name in os.listdir(api_dir):
        if module_name.endswith(".py") and module_name != "__init__.py":
            module_path = f"{api_dir}.{module_name[:-3]}"
            print(module_path)
            module = importlib.import_module(module_path)
            if hasattr(module, "router"):
                print(f"/api/{module_name[:-3]}")
                app.include_router(module.router, prefix=f"/api/{module_name[:-3]}", tags=[module_name[:-3]])

# Include all routers
include_routers()
# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Repair Management System"}