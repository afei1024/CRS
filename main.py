import uvicorn
from core.settings import settings



def main():
    #  uvicorn.run第一个参数app传输字符串时 格式为：‌"模块路径:应用实例变量名"‌，例如：
    uvicorn.run(
        "app:app",
        # IP
        host=settings.API_HOST,
        # 端口号
        port=settings.API_PORT,
        # 日志级别, lower 将字符串转为小写
        log_level=settings.LOG_LEVEL.lower(),
        # 日志配置
        # log_config=log_config(),
        # workers=settings.WORKERS,
        # 允许访问的IP
        forwarded_allow_ips=settings.HOST_IP,
        # 证书路径
        # ssl_keyfile=settings.TLS_PRIVATE_KEY_PATH,
        # ssl_certfile=settings.TLS_CERTIFICATE_PATH,
    )



if __name__ == "__main__":
    # uvicorn.run(
    #    'main:app',
    #     host="0.0.0.0",
    #     port=8000,
    #     reload=True
    # )
    main()