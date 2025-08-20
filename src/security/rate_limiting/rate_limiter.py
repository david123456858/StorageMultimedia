# from fastapi import HTTPException, Request
# from fastapi.responses import JSONResponse
# from datetime import datetime, timedelta
# from typing import Dict, Tuple
# import time

# class RateLimiter:
#     def __init__(self, requests_per_minute: int = 60):
#         self.requests_per_minute = requests_per_minute
#         self.requests: Dict[str, list] = {}
        
#     async def __call__(self, request: Request):
#         client_ip = request.client.host
#         now = time.time()
        
#         # Limpiar registros antiguos
#         if client_ip in self.requests:
#             self.requests[client_ip] = [
#                 req_time for req_time in self.requests[client_ip]
#                 if req_time > now - 60
#             ]
#         else:
#             self.requests[client_ip] = []
            
#         # Verificar límite
#         if len(self.requests[client_ip]) >= self.requests_per_minute:
#             raise HTTPException(
#                 status_code=429,
#                 detail="Demasiadas solicitudes. Por favor, intente más tarde."
#             )
            
#         # Registrar nueva solicitud
#         self.requests[client_ip].append(now)
        
#         return None
