from fastapi import UploadFile
from fastapi.responses import JSONResponse

from src.feacture.multimedia.caseuse.multimedia import CaseUseMultimedia
from src.feacture.multimedia.caseuse.caseUseFindByTag import caseUseFindsByTags
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoCreate, MultimediaDtoUpdate
from src.shared.utils.response.response_factory import ResponseFactory



class ControllerMultimedia:
    def __init__(self, case_use: CaseUseMultimedia,case_use_finds:caseUseFindsByTags):
        self.case_use = case_use
        self.case_use_find = case_use_finds
## part of case use crud -----------------------------------------------------------------
    async def create_multimedia(self, email_client:str ,file:UploadFile):
        response = await self.case_use.create_multimedia(email_client,file)        
        ResponseFactory().create_process(response)
        

    def get_all_multimedia(self,email_client: str,page:int,size_page:int):
        response = self.case_use.get_all_multimedia(email_client,page,size_page)
        ResponseFactory().create_process(response)

    def get_multimedia_by_id(self, id: int):
        result = self.case_use.get_multimedia_by_id(id)
        if not result:
            return JSONResponse(content={"error": "Multimedia no encontrada"}, status_code=404)
        return JSONResponse(content={"data": {"id": result.id, "name": result.name, "url": result.url, "type": result.type}}, status_code=200)

    def update_multimedia(self, public_id:str, dto: MultimediaDtoUpdate):
        response = self.case_use.update_multimedia(public_id, dto)
        ResponseFactory().create_process(response)

    def delete_multimedia(self, email_client: str):
        response = self.case_use.delete_multimedia(email_client)
        ResponseFactory().create_process(response)

    ## part of case use find by tags -------------------------------------------------------------------
    ## Se puede convertir en algo mas facil
    def find_by_tag_favorite(self,email_client:str):
        response = self.case_use_find.find_by_tag_favorite(email_client)
        ResponseFactory().create_process(response)
    
    def find_by_tag_private(self,email_client:str):
        response = self.case_use_find.find_by_tag_private(email_client)
        ResponseFactory().create_process(response)
    
    def find_by_tag_deleted(self,email_client:str):
        response = self.case_use_find.find_by_tag_deleted(email_client)
        ResponseFactory().create_process(response)
        
    def find_by_tag_archived(self,email_client:str):
        response = self.case_use_find.find_by_tag_archived(email_client)
        ResponseFactory().create_process(response)
    
    