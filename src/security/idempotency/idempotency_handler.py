from fastapi import FastAPI, HTTPException,Request,Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import hashlib

class handlerIdempotency(BaseHTTPMiddleware):
    def __init__(self,app:FastAPI,ttl:int = 10) -> None:
        """
        Args:
            app: La aplicación FastAPI
            ttl: Tiempo de vida de las entradas en segundos (por defecto 1 hora)
        """
        super().__init__(app)
        # self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl_seconds = ttl   
    
    async def get_idempotency(self,requests:Request,call_next):
        if requests.method not in ["POST", "PUT", "PATCH"]:
            return await call_next(requests)
        
        idempotency_key = requests.headers.get('Idempotency-Key')
        if not idempotency_key:
            return
        
        request_key = self._decode_idempotency(requests,idempotency_key)
        response_cached = self._get_cached(request_key)
        
        if response_cached:
            return JSONResponse(content=response_cached,status_code=200,headers={
                "X-Idempotency-Replayed": "true"
            })
        
        response = await call_next()
        
        if 200 <= response.status_code < 300:
            self._add_reponse_cached(response)
        
        return response
    
    async def _decode_idempotency(self,request:Request, key_idemptency:str):
        """
        De esta manera la idempotencia es unica por metodo y por tipo de informacion que viene del cuerpo
        """
        body = await request.body()
        content_key = f"{request.method}:{request.url.path}:{key_idemptency}:{body.decode()}"
        return hashlib.sha256(content_key.encode()).hexdigest()
    
    
    def _get_cached(self,key):
        return
    
    def _add_reponse_cached(self,response):
        return