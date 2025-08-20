# from fastapi import FastAPI, Depends
# from fastapi.middleware.base import BaseHTTPMiddleware
# from src.security.jwt.jwt_handler import JWTHandler
# from src.security.rate_limiting.rate_limiter import RateLimiter
# from src.security.idempotency.idempotency_handler import IdempotencyMiddleware

# def configure_security(app: FastAPI):
#     # JWT Handler
#     jwt_handler = JWTHandler()
    
#     # Rate Limiting
#     rate_limiter = RateLimiter(requests_per_minute=60)
#     app.add_middleware(BaseHTTPMiddleware, dispatch=rate_limiter)
    
#     # Idempotency
#     idempotency_handler = IdempotencyMiddleware()
#     app.add_middleware(BaseHTTPMiddleware, dispatch=idempotency_handler)
    
#     return {
#         'jwt_handler': jwt_handler,
#         'rate_limiter': rate_limiter,
#         'idempotency_handler': idempotency_handler
#     }

# # Dependencia para proteger rutas con JWT
# def get_current_user(jwt_handler: JWTHandler = Depends()):
#     async def dependency(token = Depends(jwt_handler.verify_token)):
#         return token
#     return dependency
