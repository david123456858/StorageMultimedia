from pydantic import BaseModel
from typing import Optional

class MultimediaDtoCreate(BaseModel):
    name: str
    url: str
    type: str

class MultimediaDtoUpdate(BaseModel):
    is_favorite: Optional[bool] = None
    is_archived: Optional[bool] = None
    is_private: Optional[bool] = None
    is_deleted: Optional[bool] = None
