from src.feacture.videos.caseuse.video import CaseUseVideo
from src.feacture.videos.dtos.video import VideoDtoCreate, VideoDtoUpdate
from fastapi.responses import JSONResponse

class ControllerVideo:
    def __init__(self, case_use: CaseUseVideo):
        self.case_use = case_use

    def create_video(self, dto: VideoDtoCreate):
        result = self.case_use.create_video(dto)
        return JSONResponse(content={"message": "Video creado", "data": result.id}, status_code=201)

    def get_all_videos(self):
        result = self.case_use.get_all_videos()
        return JSONResponse(content={"data": [ {"id": vid.id, "name": vid.name, "url": vid.url, "duration": vid.duration, "format": vid.format} for vid in result ]}, status_code=200)

    def get_video_by_id(self, id: int):
        result = self.case_use.get_video_by_id(id)
        if not result:
            return JSONResponse(content={"error": "Video no encontrado"}, status_code=404)
        return JSONResponse(content={"data": {"id": result.id, "name": result.name, "url": result.url, "duration": result.duration, "format": result.format}}, status_code=200)

    def update_video(self, id: int, dto: VideoDtoUpdate):
        result = self.case_use.update_video(id, dto)
        if not result:
            return JSONResponse(content={"error": "Video no encontrado"}, status_code=404)
        return JSONResponse(content={"message": "Video actualizado", "data": result.id}, status_code=200)

    def delete_video(self, id: int):
        result = self.case_use.delete_video(id)
        if not result:
            return JSONResponse(content={"error": "Video no encontrado"}, status_code=404)
        return JSONResponse(content={"message": "Video eliminado"}, status_code=200)
