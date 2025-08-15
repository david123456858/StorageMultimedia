from src.shared.utils.result import  SuccessProccess, FailureProccess

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
    
    async def upload_file(self,file):
        try:
            return SuccessProccess(200,'')
        except Exception as e:
            return FailureProccess(500,'')