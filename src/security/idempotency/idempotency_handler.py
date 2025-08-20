# from fastapi import Request, HTTPException
# from typing import Dict, Any
# import time
# import hashlib
# import json

# class IdempotencyMiddleware:
#     def __init__(self, cache_time: int = 300):  # 5 minutos por defecto
#         self.cache_time = cache_time
#         self.cache: Dict[str, tuple[float, Any]] = {}
        
#     def _generate_idempotency_key(self, request: Request) -> str:
#         """Genera una clave única basada en la solicitud"""
#         body = request.body() if request.method in ['POST', 'PUT', 'PATCH'] else b''
#         content = f"{request.method}:{request.url}:{body}"
#         return hashlib.sha256(content.encode()).hexdigest()
        
#     async def __call__(self, request: Request):
#         if request.method not in ['POST', 'PUT', 'PATCH']:
#             return None
            
#         idempotency_key = request.headers.get('X-Idempotency-Key')
#         if not idempotency_key:
#             return None
            
#         now = time.time()
        
#         # Limpiar entradas antiguas
#         self.cache = {
#             k: v for k, v in self.cache.items()
#             if v[0] > now - self.cache_time
#         }
        
#         # Verificar si existe una respuesta en caché
#         if idempotency_key in self.cache:
#             timestamp, response = self.cache[idempotency_key]
#             if timestamp > now - self.cache_time:
#                 return response
                
#         return None
        
#     def cache_response(self, idempotency_key: str, response: Any):
#         """Almacena la respuesta en caché"""
#         if idempotency_key:
#             self.cache[idempotency_key] = (time.time(), response)
