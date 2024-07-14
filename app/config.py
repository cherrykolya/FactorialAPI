from functools import lru_cache

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # Service
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI example application"
    version: str = "0.0.0"
    allowed_hosts: list[str] = ["*"]

    CACHE_WARM_LIMIT: int = 10000


@lru_cache
def get_settings() -> AppSettings:
    """
    Получение и кэширование настроек проекта
    Можно использовать как зависимость внутри эндпойнта:
        from app.core import config
        settings: config.AppSettings = Depends(config.get_settings)
    """
    return AppSettings()
