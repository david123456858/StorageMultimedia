from pydantic import BaseModel

class VideoDtoCreate(BaseModel):
    name: str
    url: str
    duration: int
    format: str

class VideoDtoUpdate(BaseModel):
    name: str | None = None
    url: str | None = None
    duration: int | None = None
    format: str | None = None
