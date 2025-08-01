from fastapi import UploadFile
from fastapi.responses import JSONResponse

from src.feacture.multimedia.caseuse.multimedia import CaseUseMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoCreate, MultimediaDtoUpdate



class ControllerMultimedia:
    def __init__(self, case_use: CaseUseMultimedia):
        self.case_use = case_use

    async def create_multimedia(self, email_client:str ,file:UploadFile):
        response = await self.case_use.create_multimedia(email_client,file)
        
        if not response['success']:
            return JSONResponse({"error":response['error']},response['statusCode'])
        
        return JSONResponse({"message":response['value']},response['statusCode']) 

    def get_all_multimedia(self,email_client:str,page:int,size_page:int):
        response = self.case_use.get_all_multimedia(email_client,page,size_page)
        
        if not response['success']:
            return JSONResponse({"error":response['error']},response['statusCode'])
        
        return JSONResponse({"message":response['value']},response['statusCode']) 

    def get_multimedia_by_id(self, id: int):
        result = self.case_use.get_multimedia_by_id(id)
        if not result:
            return JSONResponse(content={"error": "Multimedia no encontrada"}, status_code=404)
        return JSONResponse(content={"data": {"id": result.id, "name": result.name, "url": result.url, "type": result.type}}, status_code=200)

    def update_multimedia(self, public_id:str, dto: MultimediaDtoUpdate):
        response = self.case_use.update_multimedia(public_id, dto)
        if not response['success']:
            return JSONResponse({"error":response['error']},response['statusCode'])
        
        return JSONResponse({"message":response['value']},response['statusCode']) 

    def delete_multimedia(self, id: str):
        result = self.case_use.delete_multimedia(id)
        if not result:
            return JSONResponse(content={"error": "Multimedia no encontrada"}, status_code=404)
        return JSONResponse(content={"message": "Multimedia eliminada"}, status_code=200)
