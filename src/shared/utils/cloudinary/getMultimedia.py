
from cloudinary.utils import cloudinary_url
from typing import List

from src.feacture.multimedia.entity.multimedia import Multimedia


def get_cloudinary_multimedia(list_multimedia:List[Multimedia]):
    try:
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
    except Exception as e:
        return e