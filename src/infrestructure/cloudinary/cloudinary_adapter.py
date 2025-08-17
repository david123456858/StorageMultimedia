from src.shared.utils.result import  SuccessProccess, FailureProccess
from fastapi import UploadFile
from cloudinary.uploader import upload
# El desarrollo de este patron de diseño excelente, es el adapter desacoplando la 
# Logica de los servicios sin tener que afectar directamente la lofica principal del caso de uso
# o de algun service.

class CloudinaryAdapter:
    """
    Clase de acoplamiento para el manejo total de cloudinary
    """
    def __init__(self,config):
        self.config = config
        pass
    
    async def upload_file(self,file:UploadFile):
        try:
            result = upload(file,resource_type="auto")
            return result
        except Exception as e:
            return False