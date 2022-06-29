from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.schemas import Pessoa
from infra.sqlalchemy.repositorios.repositorio_pessoa import RepositorioPessoa
from infra.sqlalchemy.config.database import get_db



router = APIRouter()

@router.post("/pessoas/", status_code=status.HTTP_201_CREATED, response_model=Pessoa)
def create_pessoa(pessoa: Pessoa, db: Session = Depends(get_db)):
    creted_pessoa = RepositorioPessoa(db).create_pessoa(pessoa)
    # Incluir excessão para não permitir inserir pessoa com o mesmo cpf
    return creted_pessoa