from datetime import datetime, timedelta
from typing import Any, Dict
from fastapi import FastAPI, HTTPException,Request,Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import hashlib

class handlerIdempotency(BaseHTTPMiddleware):
    def __init__(self,app ,ttl:int = 10) -> None:
        """
        Args:
            app: La aplicación FastAPI
            ttl: Tiempo de vida de las entradas en segundos (por defecto 1 hora)
        """
        super().__init__(app)
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl_seconds = ttl  
        
    async def dispatch(self, request: Request, call_next) -> Response:
        """Método principal que intercepta todas las requests"""
        response = await self.get_idempotency(request, call_next)
        print(response)
        if not response:
            return JSONResponse({"message": "mala"},400)
        
        if isinstance(response, Response):
            return response
        
        return JSONResponse(response,200)
        
            
    async def get_idempotency(self, requests: Request, call_next):
        try:
            if requests.method not in ["POST", "PUT", "PATCH"]:
                return await call_next(requests)
        
            idempotency_key = requests.headers.get('Idempotency-Key')
        
            if not idempotency_key:
                return JSONResponse('pongase pilas primo',422)
        
            request_key = await self._decode_idempotency(requests, idempotency_key)
            response_cached = await self._get_cached(request_key)
        
            if response_cached:
                # response_cached is a dict with content, status_code, headers
                return JSONResponse(content=response_cached["content"], status_code=response_cached["status_code"], headers={
                    **response_cached.get("headers", {}),
                    "X-Idempotency-Replayed": "true"
                })
        
            response = await call_next(requests)
            print(response)
            if 200 <= response.status_code < 300:
                await self._add_reponse_cached(response, request_key)
            
            return response    
        except Exception as e:
            print(e)
            
        
    async def _decode_idempotency(self, request: Request, key_idemptency: str) -> str:
        """
        De esta manera la idempotencia es unica por metodo y por tipo de informacion que viene del cuerpo
        """
        body = await request.body()
        content_key = f"{request.method}:{request.url.path}:{key_idemptency}:{body.decode()}"
        return hashlib.sha256(content_key.encode()).hexdigest()
        
    async def _get_cached(self, request_key):
        return
        
        
    
    async def _add_reponse_cached(self, response, request_key):
        return