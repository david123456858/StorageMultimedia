from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated


## dtos user validation
class userDtoRegiter(BaseModel):
    name : Annotated[str,StringConstraints(min_length=10,max_length=50)]
    email : EmailStr
    password:  Annotated[str,StringConstraints(min_length=8,max_length=100)]


class userDtoLogin(BaseModel):
    email : EmailStr 
    password : str