from typing import Any

from fastapi import APIRouter, Depends, Query

from app.services import CacheServiceInterface, get_cache_service

router = APIRouter(tags=["Factorial"])


@router.get("/factorial")
def factorial(n: int = Query(le=10_000), cache_service: CacheServiceInterface = Depends(get_cache_service)) -> Any:
    if value := cache_service.get(n):
        return {"value": str(value)}

    cache_service.set(n)
    return {"value": str(cache_service.get(n))}


@router.get("/factorial-threadsafe")
def factorial_threadsafe(
    n: int = Query(le=10_000), cache_service: CacheServiceInterface = Depends(get_cache_service)
) -> Any:
    return {"value": cache_service.get(n)}
