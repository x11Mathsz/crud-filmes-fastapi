from pydantic import BaseModel
from typing import Optional

class FilmeBase(BaseModel):
    titulo: str
    ano: str
    genero: str
    nota: float

class FilmeCreate(FilmeBase):
    pass

class Filme(FilmeBase):
    id: int
    
    class Config:
        from_attributes = True
