from pydantic import BaseModel, EmailStr
from typing import Optional


class Pessoa(BaseModel):
    id: Optional[int] = None
    nome: str
    rg: str
    cpf: str
    email: EmailStr
    idade: int
    formacao: str
    endereco: str
    superuser: bool = False

    class Config:
        orm_mode = True

