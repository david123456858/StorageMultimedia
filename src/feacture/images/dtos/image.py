from pydantic import BaseModel

class ImageDtoCreate(BaseModel):
    # Agrega los campos necesarios para crear una imagen
    name: str
    url: str

class ImageDtoUpdate(BaseModel):
    # Agrega los campos necesarios para actualizar una imagen
    name: str | None = None
    url: str | None = None
