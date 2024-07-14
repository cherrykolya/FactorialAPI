from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.services import get_cache_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    cache_service = get_cache_service()
    cache_service.start(settings.CACHE_WARM_LIMIT)
    yield
