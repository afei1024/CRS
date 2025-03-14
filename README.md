# 问题上报系统
想写一个大学维修上报系统， 已经离开开发两年多了， 作为一个熟悉练手项目
## 一、技术选型与核心架构
* 项目架构:B/S 
* 开发语言：python3.11
* 数据库：mysql
* 后端框架：FastAPI
* 前端：Vue.js
* 缓存数据库：Redis
* 中间件（ORM）：SQLAlchemy
## 二、关键开发考量
### 1.前后端分离实现
* API 设计‌：遵循 RESTful 规范，定义清晰的接口文档（如 Swagger）‌
* 通信安全‌：采用 HTTPS + JWT 鉴权，敏感数据（如用户手机号）加密传输‌
### 2.小程序适配优化
该程序后续会做小程序开发，可以做好前期准备，减少后续调整
* 性能优化‌：
  * 减少首屏加载时间：分包加载、图片懒加载‌
  * 本地缓存：利用微信小程序 Storage API 缓存静态数据（如维修类型列表）‌
* 用户体验‌：集成微信原生能力（如扫码报修、地理位置获取）提升便捷性‌ 
### 3. ‌运维与部署
后续部署，根据开打情况， 可能会使用最为省事的“宝塔”进行安装部署
* 容器化部署‌：使用 Docker + Kubernetes 管理后端服务，实现弹性扩缩容‌
* 监控与日志‌：集成 Prometheus（性能监控） + ELK（日志分析）‌
* 云服务‌：校内云平台




## 三、 项目内容
### （一）、文件布局设计

    project/
    api/                    # API 路由模块
        auth_router.py      # 登录、注册、忘记密码等认证相关路由
        issue_report.py     # 问题上报相关路由
        management.py       # 报修单管理相关路由
        user_profile.py     # 用户个人中心相关路由
        technician.py       # 维修人员相关路由
        statistics.py       # 统计与报表相关路由
        notification.py     # 通知与提醒相关路由
        settings.py         # 系统设置相关路由
        logs.py            # 日志与监控相关路由
        feedback.py        # 用户反馈相关路由
    service/                # 业务逻辑层
        auth_service.py     # 认证相关业务逻辑
        repair_service.py   # 报修相关业务逻辑
        user_service.py     # 用户相关业务逻辑
        technician_service.py # 维修人员相关业务逻辑
        statistics_service.py # 统计相关业务逻辑
        notification_service.py # 通知相关业务逻辑
        settings_service.py # 系统设置相关业务逻辑
        logs_service.py     # 日志相关业务逻辑
        feedback_service.py # 反馈相关业务逻辑
    models/                 # 数据库模型
        user_model.py       # 用户模型
        repair_model.py     # 报修单模型
        notification_model.py # 通知模型
        feedback_model.py   # 反馈模型
    config/                 # 配置类（数据库、Redis）
        db_config.py        # 数据库配置
        redis_config.py     # Redis配置
    utils/                  # 工具类（加密、日志）
        security.py         # 加密工具
        logger.py           # 日志工具
    static/                 # 静态文件（CSS/JS）
        style.css           # 前端样式
    templates/              # HTML 模板
        login.html         # 登录页面模板
    app.py                  # 整合路由，集中注册所有子路由
    main.py                 # 应用入口
    requirements.txt        # 依赖文件
    .env                    # 环境变量配置

### （二）、.数据库设计
### 1. MySQL 表结构
* 用户表
```mysql
CREATE TABLE user (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,  -- 用户名
  password VARCHAR(100) NOT NULL,        -- 加密后的密码
  role ENUM('student', 'admin', 'repairer') NOT NULL  -- 角色区分权限‌:ml-citation{ref="2" data="citationList"}
);

```
* 报修表
```mysql
CREATE TABLE repair_order (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,                   -- 关联用户ID
  description TEXT NOT NULL,              -- 报修描述
  status ENUM('pending', 'processing', 'completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user(id)
);

```
### 2. Redis 使用场景
* 缓存高频查询数据‌（如维修人员列表、报修状态统计）‌
* 会话管理‌（存储 JWT 令牌或用户登录状态）‌

### （三）、网站设计及前后端代码构想实现
### （一）、文件布局设计

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
        app.py                  # 整合路由，集中注册所有子路由
        main.py                 # 应用入口
        requirements.txt
        .env                        # 环境变量配置
#### 1. 登录页面
**功能需求：**
- **用户登录**：用户可以通过输入用户名和密码进行登录。
- **角色区分**：根据用户角色（学生、管理员、维修人员）跳转到不同的页面。
- **忘记密码**：提供忘记密码功能，用户可以通过邮箱或手机号重置密码。
- **注册功能**：提供用户注册入口，新用户可以通过填写基本信息进行注册。

**前端实现：**
- **UI设计**：简洁的登录表单，包含用户名、密码输入框，登录按钮，以及忘记密码和注册链接。
- **表单验证**：前端对用户名和密码进行基本格式验证，如非空、密码长度等。
- **交互设计**：登录成功后，根据用户角色跳转到相应的页面；登录失败时，显示错误提示信息。

**后端实现：**
- **API接口**：提供登录接口 `/api/auth/login`，接收用户名和密码，返回 JWT 令牌。
- **鉴权逻辑**：验证用户名和密码，生成 JWT 令牌并返回给前端。
- **密码加密**：使用 BCryptPasswordEncoder 对密码进行哈希存储和验证。

#### 2. 问题上报页面
**功能需求：**
- **问题描述**：用户可以填写报修问题的详细描述。
- **上传图片**：用户可以选择上传问题相关的图片，最多上传3张。
- **选择维修类型**：用户可以从预定义的维修类型列表中选择问题类型。
- **提交报修**：用户提交报修单后，系统生成报修单号并显示提交成功信息。

**前端实现：**
- **UI设计**：表单包含问题描述文本框、图片上传组件、维修类型下拉菜单和提交按钮。
- **表单验证**：前端对问题描述进行非空验证，图片上传限制为3张。
- **交互设计**：提交成功后，显示报修单号和成功提示；提交失败时，显示错误提示信息。

**后端实现：**
- **API接口**：提供报修提交接口 `/api/repair/submit`，接收问题描述、图片和维修类型，返回报修单号。
- **数据存储**：将报修信息存储到 MySQL 数据库的 `repair_order` 表中。
- **图片处理**：将上传的图片存储到服务器或云存储，并在数据库中保存图片路径。

#### 3. 管理页面
**功能需求：**
- **报修单管理**：管理员可以查看所有报修单，并根据状态（待处理、处理中、已完成）进行筛选。
- **报修单详情**：管理员可以查看报修单的详细信息，包括问题描述、图片、报修时间等。
- **分配维修人员**：管理员可以将报修单分配给指定的维修人员。
- **状态更新**：维修人员可以更新报修单的状态（如从“待处理”改为“处理中”）。
- **统计报表**：管理员可以查看报修单的统计信息，如各类维修类型的数量、处理时长等。

**前端实现：**
- **UI设计**：表格展示报修单列表，包含筛选条件、报修单详情按钮、分配维修人员下拉菜单和状态更新按钮。
- **交互设计**：点击报修单详情按钮，弹出模态框显示详细信息；分配维修人员和更新状态时，实时更新表格数据。

**后端实现：**
- **API接口**：
  - 获取报修单列表接口 `/api/repair/list`，支持状态筛选。
  - 获取报修单详情接口 `/api/repair/detail/{id}`。
  - 分配维修人员接口 `/api/repair/assign`。
  - 更新报修单状态接口 `/api/repair/update-status`。
- **数据查询**：从 MySQL 数据库查询报修单信息，并根据筛选条件返回结果。
- **权限控制**：只有管理员和维修人员可以访问管理页面和相关接口。

#### 4. 用户个人中心
**功能需求：**
- **个人信息管理**：用户可以查看和修改个人信息，如用户名、手机号、邮箱等。
- **报修记录**：用户可以查看自己提交的报修单记录及其状态。
- **修改密码**：用户可以修改登录密码。

**前端实现：**
- **UI设计**：个人信息表单、报修记录列表、修改密码表单。
- **交互设计**：修改信息或密码后，显示成功提示；报修记录列表支持点击查看详情。

**后端实现：**
- **API接口**：
  - 获取个人信息接口 `/api/user/profile`。
  - 更新个人信息接口 `/api/user/update-profile`。
  - 获取报修记录接口 `/api/user/repair-history`。
  - 修改密码接口 `/api/user/change-password`。
- **数据查询**：从 MySQL 数据库查询用户信息和报修记录。
- **权限控制**：只有登录用户可以访问个人中心相关接口。

#### 5. 维修人员页面
**功能需求：**
- **任务列表**：维修人员可以查看分配给自己的报修单任务。
- **任务详情**：维修人员可以查看报修单的详细信息，包括问题描述、图片等。
- **状态更新**：维修人员可以更新报修单的状态（如从“处理中”改为“已完成”）。

**前端实现：**
- **UI设计**：任务列表表格，包含任务详情按钮和状态更新按钮。
- **交互设计**：点击任务详情按钮，弹出模态框显示详细信息；更新状态时，实时更新表格数据。

**后端实现：**
- **API接口**：
  - 获取任务列表接口 `/api/repair/tasks`。
  - 获取任务详情接口 `/api/repair/task-detail/{id}`。
  - 更新任务状态接口 `/api/repair/update-task-status`。
- **数据查询**：从 MySQL 数据库查询分配给当前维修人员的报修单任务。
- **权限控制**：只有维修人员可以访问维修人员页面和相关接口。

#### 6. 统计与报表页面
**功能需求：**
- **报修单统计**：管理员可以查看报修单的统计信息，如各类维修类型的数量、处理时长等。
- **图表展示**：通过柱状图、饼图等形式展示统计结果。

**前端实现：**
- **UI设计**：图表展示区域，包含筛选条件和图表类型选择。
- **交互设计**：根据筛选条件动态更新图表数据。

**后端实现：**
- **API接口**：提供报修单统计接口 `/api/repair/statistics`，支持按时间、维修类型等条件筛选。
- **数据查询**：从 MySQL 数据库查询报修单统计信息，并返回给前端。
- **权限控制**：只有管理员可以访问统计与报表页面和相关接口。

#### 7. 通知与提醒
**功能需求：**
- **报修单状态通知**：当报修单状态发生变化时，系统通过站内消息或邮件通知相关用户。
- **任务分配通知**：当报修单被分配给维修人员时，系统通过站内消息或邮件通知维修人员。

**前端实现：**
- **UI设计**：站内消息通知中心，显示未读消息和已读消息。
- **交互设计**：点击消息可以查看详细信息，并标记为已读。

**后端实现：**
- **API接口**：
  - 获取消息列表接口 `/api/notification/list`。
  - 标记消息为已读接口 `/api/notification/mark-as-read`。
- **消息推送**：在报修单状态变化或任务分配时，生成消息并推送给相关用户。
- **权限控制**：只有登录用户可以访问通知与提醒相关接口。

#### 8. 系统设置
**功能需求：**
- **维修类型管理**：管理员可以添加、编辑、删除维修类型。
- **用户管理**：管理员可以查看、编辑、删除用户信息。
- **角色管理**：管理员可以管理用户角色（学生、管理员、维修人员）。

**前端实现：**
- **UI设计**：维修类型管理表格、用户管理表格、角色管理表格。
- **交互设计**：支持添加、编辑、删除操作，操作后实时更新表格数据。

**后端实现：**
- **API接口**：
  - 维修类型管理接口 `/api/settings/repair-types`。
  - 用户管理接口 `/api/settings/users`。
  - 角色管理接口 `/api/settings/roles`。
- **数据操作**：对 MySQL 数据库中的维修类型、用户、角色表进行增删改查操作。
- **权限控制**：只有管理员可以访问系统设置相关接口。

#### 9. 日志与监控
**功能需求：**
- **操作日志**：记录用户的关键操作（如登录、报修提交、状态更新等）。
- **系统监控**：监控系统的性能指标（如 CPU、内存使用率等）。

**前端实现：**
- **UI设计**：操作日志表格、系统监控图表。
- **交互设计**：支持按时间、操作类型等条件筛选日志；监控图表实时更新。

**后端实现：**
- **API接口**：
  - 获取操作日志接口 `/api/logs/operations`。
  - 获取系统监控数据接口 `/api/monitoring/metrics`。
- **数据存储**：将操作日志存储到 MySQL 数据库或日志文件；系统监控数据通过 Prometheus 采集。
- **权限控制**：只有管理员可以访问日志与监控相关接口。

#### 10. 安全与权限
**功能需求：**
- **权限控制**：根据用户角色（学生、管理员、维修人员）控制页面和接口的访问权限。
- **数据加密**：敏感数据（如用户密码）在传输和存储时进行加密。
- **会话管理**：使用 JWT 令牌管理用户会话，确保用户登录状态的安全性。

**前端实现：**
- **UI设计**：无特定 UI，通过路由守卫控制页面访问权限。
- **交互设计**：用户未登录时，重定向到登录页面；用户无权限时，显示无权限提示。

**后端实现：**
- **API接口**：所有接口均需进行 JWT 鉴权，验证用户身份和权限。
- **数据加密**：使用 HTTPS 加密传输数据，使用 BCryptPasswordEncoder 加密存储密码。
- **会话管理**：使用 Redis 存储 JWT 令牌，实现会话管理和令牌失效机制。

#### 11. 扩展功能
**功能需求：**
- **微信小程序适配**：后续开发微信小程序版本，适配移动端使用场景。
- **第三方登录**：支持微信、QQ 等第三方登录方式。
- **多语言支持**：支持中英文切换，适配国际化需求。

**前端实现：**
- **UI设计**：根据微信小程序设计规范，优化页面布局和交互。
- **交互设计**：支持微信原生能力（如扫码报修、地理位置获取）提升便捷性。

**后端实现：**
- **API接口**：提供微信小程序专用接口，支持微信登录、扫码报修等功能。
- **数据存储**：将微信用户信息存储到 MySQL 数据库，关联系统用户表。
- **权限控制**：微信小程序用户通过微信登录后，获取系统用户权限。

#### 12. 部署与运维
**功能需求：**
- **容器化部署**：使用 Docker + Kubernetes 管理后端服务，实现弹性扩缩容。
- **监控与日志**：集成 Prometheus（性能监控） + ELK（日志分析）。
- **云服务**：部署到校内云平台，确保系统的高可用性和可扩展性。

**前端实现：**
- **UI设计**：无特定 UI，通过 CI/CD 工具自动化部署前端代码。

**后端实现：**
- **API接口**：无特定 API，通过 Dockerfile 和 Kubernetes 配置文件定义服务部署。
- **数据存储**：使用云数据库（如 RDS）和云存储（如 OSS）确保数据的高可用性。
- **权限控制**：通过 Kubernetes 的 RBAC 机制控制服务的访问权限。

#### 13. 测试与验收
**功能需求：**
- **单元测试**：对关键模块（如登录、报修提交、状态更新）进行单元测试。
- **集成测试**：对前后端接口进行集成测试，确保接口的正确性和稳定性。
- **用户验收测试**：邀请用户进行验收测试，收集反馈并优化系统。

**前端实现：**
- **UI设计**：无特定 UI，通过测试工具（如 Jest）编写前端单元测试。
- **交互设计**：通过自动化测试工具（如 Cypress）模拟用户操作进行集成测试。

**后端实现：**
- **API接口**：通过测试工具（如 Pytest）编写后端单元测试和集成测试。
- **数据存储**：使用测试数据库（如 SQLite）进行测试，确保数据操作的准确性。
- **权限控制**：通过测试工具模拟不同角色用户，验证权限控制的正确性。

#### 14. 文档与培训
**功能需求：**
- **用户手册**：编写详细的用户手册，指导用户如何使用系统。
- **开发文档**：编写详细的开发文档，记录系统的设计思路、技术选型和实现细节。
- **培训材料**：准备培训材料，对管理员和维修人员进行系统使用培训。

**前端实现：**
- **UI设计**：无特定 UI，通过 Markdown 编写用户手册和开发文档。
- **交互设计**：通过在线文档平台（如 GitBook）发布文档，方便用户查阅。

**后端实现：**
- **API接口**：通过 Swagger 自动生成 API 文档，方便开发人员查阅。
- **数据存储**：无特定数据存储，通过文档管理系统（如 Confluence）管理文档。
- **权限控制**：通过文档管理系统控制文档的访问权限，确保文档的安全性。

#### 15. 维护与升级
**功能需求：**
- **Bug 修复**：及时修复用户反馈的 Bug，确保系统的稳定性。
- **功能升级**：根据用户需求和市场变化，持续优化和升级系统功能。
- **版本管理**：使用 Git 进行版本管理，记录每次更新和修复的内容。

**前端实现：**
- **UI设计**：无特定 UI，通过 Git 提交记录管理前端代码的版本。
- **交互设计**：通过 CI/CD 工具自动化部署前端代码，确保每次更新的及时性。

**后端实现：**
- **API接口**：通过 Git 提交记录管理后端代码的版本，确保每次更新的可追溯性。
- **数据存储**：通过数据库迁移工具（如 Alembic）管理数据库结构的变更。
- **权限控制**：通过 Git 分支管理机制控制代码的访问权限，确保代码的安全性。

#### 16. 用户反馈与改进
**功能需求：**
- **反馈收集**：提供用户反馈入口，收集用户对系统的意见和建议。
- **需求分析**：分析用户反馈，提炼出系统改进的需求。
- **迭代开发**：根据用户需求和市场变化，持续迭代开发系统功能。

**前端实现：**
- **UI设计**：提供反馈表单，用户可以通过表单提交反馈。
- **交互设计**：提交反馈后，显示成功提示；反馈内容通过站内消息或邮件通知管理员。

**后端实现：**
- **API接口**：提供反馈提交接口 `/api/feedback/submit`，接收用户反馈内容。
- **数据存储**：将用户反馈存储到 MySQL 数据库的 `feedback` 表中。
- **权限控制**：只有登录用户可以提交反馈，管理员可以查看反馈内容。

#### 17. 数据备份与恢复
**功能需求：**
- **数据备份**：定期备份系统数据，确保数据的安全性。
- **数据恢复**：在数据丢失或损坏时，能够快速恢复数据。

**前端实现：**
- **UI设计**：无特定 UI，通过备份工具自动化备份前端代码和静态资源。
- **交互设计**：通过 CI/CD 工具自动化部署前端代码，确保每次更新的及时性。

**后端实现：**
- **API接口**：无特定 API，通过备份工具（如 mysqldump）自动化备份数据库。
- **数据存储**：将备份数据存储到云存储（如 OSS）或本地存储，确保数据的安全性。
- **权限控制**：通过备份工具的访问控制机制，确保备份数据的安全性。

#### 18. 性能优化
**功能需求：**
- **数据库优化**：优化数据库查询语句，减少查询时间。
- **缓存优化**：使用 Redis 缓存高频查询数据，减少数据库压力。
- **前端优化**：优化前端代码，减少页面加载时间。

**前端实现：**
- **UI设计**：无特定 UI，通过代码压缩、图片懒加载等技术优化前端性能。
- **交互设计**：通过 CDN 加速静态资源加载，提升页面加载速度。

**后端实现：**
- **API接口**：通过缓存机制（如 Redis）优化高频查询接口的性能。
- **数据存储**：通过数据库索引、分表分库等技术优化数据库查询性能。
- **权限控制**：通过缓存机制优化权限验证的性能，减少数据库查询次数。

#### 19. 安全审计
**功能需求：**
- **安全漏洞扫描**：定期进行安全漏洞扫描，发现并修复潜在的安全问题。
- **日志审计**：定期审计系统日志，发现并处理异常操作。
- **权限审计**：定期审计用户权限，确保权限分配的合理性。

**前端实现：**
- **UI设计**：无特定 UI，通过安全工具自动化扫描前端代码的安全漏洞。
- **交互设计**：通过日志审计工具自动化分析前端日志，发现异常操作。

**后端实现：**
- **API接口**：通过安全工具（如 OWASP ZAP）自动化扫描后端接口的安全漏洞。
- **数据存储**：通过日志审计工具（如 ELK）自动化分析后端日志，发现异常操作。
- **权限控制**：通过权限审计工具自动化分析用户权限，确保权限分配的合理性。

#### 20. 用户支持与帮助
**功能需求：**
- **在线帮助**：提供在线帮助文档，解答用户常见问题。
- **客服支持**：提供在线客服支持，解答用户疑问。
- **社区论坛**：建立用户社区论坛，方便用户交流经验。

**前端实现：**
- **UI设计**：提供在线帮助文档入口、在线客服入口和社区论坛入口。
- **交互设计**：点击帮助文档入口，跳转到帮助文档页面；点击在线客服入口，弹出客服对话框；点击社区论坛入口，跳转到社区论坛页面。

**后端实现：**
- **API接口**：无特定 API，通过在线帮助文档平台（如 GitBook）提供帮助文档。
- **数据存储**：通过客服系统（如 Zendesk）存储客服对话记录；通过社区论坛系统（如 Discourse）存储用户发帖内容。
- **权限控制**：通过客服系统和社区论坛系统的访问控制机制，确保用户数据

### （四）、配置文件
### （五）、注意事项
* 密码加密‌：使用 BCryptPasswordEncoder 对密码哈希存储，避免明文泄露‌
* ‌缓存一致性‌：MySQL 数据更新时需同步清理 Redis 缓存（如 @CacheEvict 注解）‌
* 事务管理‌：关键操作（如订单提交）添加 @Transactional 注解保证原子性‌
### （六）、扩展
* 注册功能‌：添加用户注册接口，密码哈希存储‌
* 验证码‌：集成第三方服务或本地生成图形验证码‌
* 日志监控‌：使用 logging 模块记录操作日志‌
* API 文档‌：通过 Swagger (/docs) 自动生成接口文档‌
