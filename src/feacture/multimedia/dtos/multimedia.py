from pydantic import BaseModel

class MultimediaDtoCreate(BaseModel):
    name: str
    url: str
    type: str

class MultimediaDtoUpdate(BaseModel):
    name: str | None = None
    url: str | None = None
    type: str | None = None
