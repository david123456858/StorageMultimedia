from src.infrestructure.cache.redis_service import RedisService

class RateLimitRepository:
    def __init__(self):
        self.redis = RedisService()
        self.window_size = 60  # 60 segundos
        
    async def increment_request_count(self, client_ip: str) -> int:
        """Incrementa y obtiene el conteo de solicitudes para una IP"""
        key = f"rate_limit:{client_ip}"
        count = await self.redis.increment(key, expiration=self.window_size)
        return count
        
    async def get_request_count(self, client_ip: str) -> int:
        """Obtiene el conteo actual de solicitudes para una IP"""
        key = f"rate_limit:{client_ip}"
        count = await self.redis.get(key)
        return int(count) if count else 0
