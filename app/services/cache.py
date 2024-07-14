import logging
from abc import abstractmethod
from functools import lru_cache

from app.utils import CustomDict


class CacheServiceInterface:
    """Интерфейс кэш сервиса"""

    @abstractmethod
    def get(self, key: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def set(self, key: int, value: int | None = None):
        raise NotImplementedError


class CacheService:
    """Имплементация кэш сервиса в качестве statefull in memory хранилища"""

    def __init__(self, data: CustomDict | None = None):
        if data is None:
            data = CustomDict()
            data[1] = 1

        self.data = data

    def get(self, key: int) -> int:
        if key not in self.data:
            return None

        return self.data[key]

    def set(self, key: int, value: int | None = None):
        if key not in self.data:
            for i in range(self.data.max_key + 1, key + 1):
                self.data[i] = self.data[i - 1] * i

    def start(self, n: int = 1_000):
        """Прогрев кэша"""
        self.set(n)

        logging.info("Cache service succsessfully started")


@lru_cache
def get_cache_service() -> CacheService:
    return CacheService()
