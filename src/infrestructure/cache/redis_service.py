from redis import Redis
from typing import Optional, Any
import json

class RedisService:
    def __init__(self):
        self.redis_client = Redis(
            host='localhost',  # Mueve esto a variables de entorno
            port=6379,
            decode_responses=True
        )

    async def set(self, key: str, value: Any, expiration: int ) -> None:
        """Guarda un valor en Redis"""
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        self.redis_client.set(key, value, ex=expiration)

    async def get(self, key: str) -> Optional[Any]:
        """Obtiene un valor de Redis"""
        value = self.redis_client.get(key)
        return value
    

    async def delete(self, key: str) -> None:
        """Elimina un valor de Redis"""
        self.redis_client.delete(key)

    async def exists(self, key: str) -> bool:
        """Verifica si una clave existe"""
        return self.redis_client.exists(key) > 0 # pyright: ignore[reportOperatorIssue]

    async def increment(self, key: str, expiration: int ) -> int:
        """Incrementa un contador"""
        pipeline = self.redis_client.pipeline()
        pipeline.incr(key)
        if expiration:
            pipeline.expire(key, expiration)
        result = pipeline.execute()
        return result[0]
