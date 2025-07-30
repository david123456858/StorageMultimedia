from src.feacture.multimedia.caseuse.multimedia import CaseUseMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoCreate, MultimediaDtoUpdate
from fastapi.responses import JSONResponse

class ControllerMultimedia:
    def __init__(self, case_use: CaseUseMultimedia):
        self.case_use = case_use

    def create_multimedia(self, dto: MultimediaDtoCreate):
        result = self.case_use.create_multimedia(dto)
        return JSONResponse(content={"message": "Multimedia creada", "data": result.id}, status_code=201)

    def get_all_multimedia(self):
        result = self.case_use.get_all_multimedia()
        return JSONResponse(content={"data": [ {"id": m.id, "name": m.name, "url": m.url, "type": m.type} for m in result ]}, status_code=200)

    def get_multimedia_by_id(self, id: int):
        result = self.case_use.get_multimedia_by_id(id)
        if not result:
            return JSONResponse(content={"error": "Multimedia no encontrada"}, status_code=404)
        return JSONResponse(content={"data": {"id": result.id, "name": result.name, "url": result.url, "type": result.type}}, status_code=200)

    def update_multimedia(self, id: int, dto: MultimediaDtoUpdate):
        result = self.case_use.update_multimedia(id, dto)
        if not result:
            return JSONResponse(content={"error": "Multimedia no encontrada"}, status_code=404)
        return JSONResponse(content={"message": "Multimedia actualizada", "data": result.id}, status_code=200)

    def delete_multimedia(self, id: int):
        result = self.case_use.delete_multimedia(id)
        if not result:
            return JSONResponse(content={"error": "Multimedia no encontrada"}, status_code=404)
        return JSONResponse(content={"message": "Multimedia eliminada"}, status_code=200)
