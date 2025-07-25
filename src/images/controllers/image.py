from src.images.caseuse.image import CaseUseImage
from src.images.dtos.image import ImageDtoCreate, ImageDtoUpdate
from fastapi.responses import JSONResponse

class ControllerImage:
    def __init__(self, case_use: CaseUseImage):
        self.case_use = case_use

    def create_image(self, dto: ImageDtoCreate):
        result = self.case_use.create_image(dto)
        return JSONResponse(content={"message": "Imagen creada", "data": result.id}, status_code=201)

    def get_all_images(self):
        result = self.case_use.get_all_images()
        return JSONResponse(content={"data": [ {"id": img.id, "name": img.name, "url": img.url} for img in result ]}, status_code=200)

    def get_image_by_id(self, id: int):
        result = self.case_use.get_image_by_id(id)
        if not result:
            return JSONResponse(content={"error": "Imagen no encontrada"}, status_code=404)
        return JSONResponse(content={"data": {"id": result.id, "name": result.name, "url": result.url}}, status_code=200)

    def update_image(self, id: int, dto: ImageDtoUpdate):
        result = self.case_use.update_image(id, dto)
        if not result:
            return JSONResponse(content={"error": "Imagen no encontrada"}, status_code=404)
        return JSONResponse(content={"message": "Imagen actualizada", "data": result.id}, status_code=200)

    def delete_image(self, id: int):
        result = self.case_use.delete_image(id)
        if not result:
            return JSONResponse(content={"error": "Imagen no encontrada"}, status_code=404)
        return JSONResponse(content={"message": "Imagen eliminada"}, status_code=200)
