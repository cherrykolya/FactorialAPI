from typing import Any

from fastapi import APIRouter, Depends, Query

from app.services import CacheService, get_cache_service

router = APIRouter(tags=["Factorial"])


@router.get("/factorial")
def health_check(n: int = Query(lt=100), cache_service: CacheService = Depends(get_cache_service)) -> Any:
    return {"value": cache_service.get(n)}
