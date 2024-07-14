import logging
from abc import abstractmethod
from functools import lru_cache
from threading import Lock

from app.utils import CustomDict

logger = logging.getLogger("uvicorn.error")


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

    def __init__(self, data: CustomDict | None = None, lock=None):
        if data is None:
            data = CustomDict()
            data[1] = 1

        if lock is None:
            self.lock = Lock()

        self.data = data

    def get(self, key: int) -> int:
        if key not in self.data:
            return None

        return self.data[key]

    def set(self, key: int, value: int | None = None):
        # если два потока одновременно пытаются изменить словарь
        # то блокируем изменения до конца работы первого
        # таким образом второй сделает проверку наличия ключа (первый мог уже рассчитать его)
        # было бы более критично если бы здесь была более тяжелая цпу нагрузка
        with self.lock:
            if not self.get(key):
                for i in range(self.data.max_key + 1, key + 1):
                    self.data[i] = self.data[i - 1] * i

    def start(self, n: int = 100):
        """Прогрев кэша"""
        self.set(n)

        logger.info("Cache service succsessfully started")

    def stop(self):
        # здесь должны быть вызовы для gracefull shutdown

        logger.info("Cache service succsessfully stoped")


@lru_cache
def get_cache_service() -> CacheService:
    return CacheService()
