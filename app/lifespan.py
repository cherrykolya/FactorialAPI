import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.services import get_cache_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    # увеличиваем максимальное кол-во символов для преобразования инта в строку
    sys.set_int_max_str_digits(1_000_000)

    settings = get_settings()
    cache_service = get_cache_service()

    # прогрев кэша
    cache_service.start(settings.CACHE_WARM_LIMIT)
    yield
