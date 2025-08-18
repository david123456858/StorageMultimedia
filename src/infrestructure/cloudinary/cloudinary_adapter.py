from src.feacture.multimedia.entity.multimedia import Multimedia

from cloudinary.uploader import upload
from cloudinary.api import delete_resources
from cloudinary.utils import cloudinary_url

from sqlalchemy import Column
from typing import List
# El desarrollo de este patron de diseño excelente, es el adapter desacoplando la 
# Logica de los servicios sin tener que afectar directamente la lofica principal del caso de uso
# o de algun service.

class CloudinaryAdapter:
    """
    Clase de acoplamiento para el manejo total de cloudinary
    """
    def __init__(self):
        pass
    
    async def upload_file(self,file:bytes):
        try:
            result = upload(file,resource_type="auto")
            return result
        except Exception as e:
            return False
        
    def  get_cloudinary_multimedia(self,list_multimedia:List[Multimedia]):
        data = []
        for value in list_multimedia:
            url,_ = cloudinary_url(value.public_id, resource_type=value.resource_type)
            thumbail_url,_ = cloudinary_url(
                value.public_id,
                resource_type=value.resource_type,
                transformation=[
                    {'width': 300, 'height': 300, 'crop': 'fill'},
                    {'quality': 'auto'},
                    {'format': 'auto'}
                ]
            ) 
                
            data.append({
                'id': value.id,
                'public_id': value.public_id,
                'resource_type': value.resource_type,
                'created_at': value.created_at.isoformat() ,##lo convierte en string el datatime
                'url': url,
                'thumbnail_url': thumbail_url
                })
    
            return data

    
    def update_multimedia(self,multimedia:Multimedia):
        ## se deja por si mas adelante se incluye algo
        return multimedia
            
        
    def delete_multimedia(self,public_ids:list[Column[str]]):
        delete_resources(public_ids)