from typing import Annotated, Any, NamedTuple
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# 在 Python 的 typing 模块中，NamedTuple 是一种定义不可变数据结构的工具，它提供了比普通元组更清晰和更具描述性的方法来组织数据。NamedTuple
# 的字段有名字，可以像访问对象的属性一样访问，而不仅仅是通过索引访问。

class ScheduleTime(NamedTuple):
    hour: int  # 小时
    minute: int  # 分钟

class AppLoggingSettings(BaseSettings):
    """
    Subset of AppSettings to only access logging-related settings.

    This is separated out from AppSettings to allow logging during construction
    of AppSettings.
    """

    TESTING: bool = False
    PRODUCTION: bool

    LOG_CONFIG_OVERRIDE: Path | None = None
    """path to custom logging configuration file"""

    LOG_LEVEL: str = "info"
    """corresponds to standard Python log levels"""

class FeatureDetails(NamedTuple):
    enabled: bool
    """Indicates if the feature is enabled or not"""
    description: str | None
    """Short description describing why the feature is not ready"""

    def __str__(self):
        s = f"Enabled: {self.enabled}"
        if not self.enabled and self.description:
            s += f"\nReason: {self.description}"
        return s

# API_HOST: str = "0.0.0.0"
API_HOST: str = "127.0.0.1"
API_PORT: int = 9000
API_DOCS: bool = True
TOKEN_TIME: int = 48
HOST_IP: str = "*"
LOG_LEVEL: str = "info"