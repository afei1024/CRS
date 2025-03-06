    project/ 
        api/                    # API 路由模块
            auth_router.py
        service/                # 业务逻辑层
            auth_service.py
        models/                 # 数据库模型
            user_model.py
        config/                 # 配置类（数据库、Redis）
            db_config.py
            redis_config.py
        utils/                  # 工具类（加密、日志）
            security.py
            logger.py
        static/                 # 静态文件（CSS/JS）
            style.css
        templates/              # HTML 模板
            login.html
            main.py                 # 应用入口
        requirements.txt
        .env                        # 环境变量配置