from src.infrestructure.cache.redis_service import RedisService
from typing import Optional, Any

class IdempotencyRepository:
    def __init__(self):
        self.redis = RedisService()
        self.default_expiration = 300  # 5 minutos
        
    async def save_response(self, idempotency_key: str, response: Any) -> None:
        """Guarda una respuesta en caché"""
        await self.redis.set(
            f"idempotency:{idempotency_key}",
            response,
            expiration=self.default_expiration
        )
        
    async def get_response(self, idempotency_key: str) -> Optional[Any]:
        """Recupera una respuesta cacheada"""
        return await self.redis.get(f"idempotency:{idempotency_key}")
        
    async def exists(self, idempotency_key: str) -> bool:
        """Verifica si existe una respuesta para la clave"""
        return await self.redis.exists(f"idempotency:{idempotency_key}")
