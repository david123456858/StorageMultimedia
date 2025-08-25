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
        self.cont = 0
        self.guardadoId = ''
        self.response_guardado = {}
        self.statu_code = 200
        self.ttl_seconds = ttl  
        
    async def dispatch(self, request: Request, call_next) -> Response:
        
        if request.method not in ['POST']:
            return await call_next(request)
        
        impotency_key = request.headers.get('Idempotency-Key')
        
        if not impotency_key:
            return JSONResponse({"Message":"Bad reques but not send hearders"},400)
        
        key_id_idempotency = await self._decode_idempotency(request,impotency_key)
        
        exist_reponse = await self._get_cached(key_id_idempotency)
        
        if exist_reponse:
            return JSONResponse(self.response_guardado,self.statu_code)
        
        response = await call_next(request)
        
        if 200<= response.status_code < 300:
            await self._add_reponse_cached(response,key_id_idempotency)
        
        
        return response
          
        
    async def _decode_idempotency(self, request: Request, key_idemptency: str) -> str:
        """
        De esta manera la idempotencia es unica por metodo y por tipo de informacion que viene del cuerpo
        """
        body = await request.body()
        content_key = f"{request.method}:{request.url.path}:{key_idemptency}:{body.decode()}"
        return hashlib.sha256(content_key.encode()).hexdigest()
        
    async def _get_cached(self, request_key):
        if request_key == self.guardadoId:
            return self.response_guardado
        return False
        
        
    
    async def _add_reponse_cached(self, response, request_key):
        self.guardadoId = request_key
        print(response)
        # self.response_guardado = response
        return