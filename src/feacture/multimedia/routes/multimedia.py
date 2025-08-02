from fastapi import APIRouter
from fastapi import File,UploadFile,Form
from pydantic import EmailStr

from src.feacture.multimedia.controllers.multimedia import ControllerMultimedia
from src.feacture.multimedia.caseuse.multimedia import CaseUseMultimedia
from src.feacture.multimedia.caseuse.caseUseFindByTag import caseUseFindsByTags
from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoUpdate

route = APIRouter(prefix='/multimedia', tags=['Multimedia'])

def routeMultimedia() -> APIRouter:
    repository = RepositoryMultimedia()
    
    case_use = CaseUseMultimedia(repository)
    case_use_finds_by_tag = caseUseFindsByTags(repository)
    
    controller = ControllerMultimedia(case_use,case_use_finds_by_tag)

    @route.post('/')
    async def create_multimedia(email_client:EmailStr = Form(...), file:UploadFile = File(...)):
        return await controller.create_multimedia(email_client,file)

    @route.get('/')
    def get_multimedia(email_client:EmailStr,page:int,size_page:int):
        return controller.get_all_multimedia(email_client,page,size_page)

    @route.get('/{id}')
    def get_multimedia_by_id(id: int):
        return controller.get_multimedia_by_id(id)

    @route.patch('/{id}')
    def update_multimedia(id:str, dto: MultimediaDtoUpdate):
        return controller.update_multimedia(id, dto)

    @route.delete('/{email_client}')
    def delete_multimedia(email_client: str):
        return controller.delete_multimedia(email_client)
    
    
    @route.get('/favorites/{email_client}')
    def get_favorites(email_client: EmailStr):
        return controller.find_by_tag_favorite(email_client)

    
    @route.get('/archived/{email_client}')
    def get_archived(email_client: EmailStr):
        return controller.find_by_tag_archived(email_client)

    
    @route.get('/deleted/{email_client}')
    def get_deleted(email_client: EmailStr):
        return controller.find_by_tag_deleted(email_client)

    
    @route.get('/private/{email_client}')
    def get_private(email_client: EmailStr):
        return controller.find_by_tag_private(email_client)

    return route
