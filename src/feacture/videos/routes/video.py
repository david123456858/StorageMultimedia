from fastapi import APIRouter
from src.feacture.videos.controllers.video import ControllerVideo
from src.feacture.videos.caseuse.video import CaseUseVideo
from src.feacture.videos.repository.video import RepositoryVideo
from src.feacture.videos.dtos.video import VideoDtoCreate, VideoDtoUpdate

route = APIRouter(prefix='/videos', tags=['Videos'])
 
def routeVideos() -> APIRouter:
    repository = RepositoryVideo()
    case_use = CaseUseVideo(repository)
    controller = ControllerVideo(case_use)

    @route.post('/')
    def create_video(dto: VideoDtoCreate):
        return controller.create_video(dto)

    @route.get('/')
    def get_videos():
        return controller.get_all_videos()

    @route.get('/{id}')
    def get_video_by_id(id: int):
        return controller.get_video_by_id(id)

    @route.put('/{id}')
    def update_video(id: int, dto: VideoDtoUpdate):
        return controller.update_video(id, dto)

    @route.delete('/{id}')
    def delete_video(id: int):
        return controller.delete_video(id)

    return route
