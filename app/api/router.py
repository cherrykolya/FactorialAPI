from typing import Any

from fastapi import APIRouter

router = APIRouter(tags=["Factorial"])


@router.get("/health-check")
def health_check() -> Any:
    return {"message": "OK"}
