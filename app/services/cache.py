import logging
from functools import lru_cache


class CacheService:
    def __init__(self, data: dict | None = None):
        if data is None:
            data = {}

        self.data = data

    def get(self, key: int) -> int:
        if key not in self.data:
            return None

        return self.data[key]

    def set(self, key: int, value: int):
        pass

    def start(self, n: int = 1_000):
        """Прогрев кэша"""
        self.data[1] = 1

        for i in range(2, n):
            self.data[i] = self.data[i - 1] * i

        logging.info("Cache service succsessfully started")


@lru_cache
def get_cache_service() -> CacheService:
    return CacheService()
