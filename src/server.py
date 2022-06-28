from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import schemas.schemas as schemas
from infra.sqlalchemy.repositorios.repositorio_pessoa import RepositorioPessoa
from infra.sqlalchemy.config.database import get_db, criar_bd

criar_bd()

app = FastAPI()


@app.post("/pessoas/", response_model=schemas.Pessoa)
def pessoa_criada(pessoa: schemas.Pessoa, db: Session = Depends(get_db)):
    creted_pessoa = RepositorioPessoa(db).create_pessoa(pessoa)
    # Incluir excessão para não permitir inserir pessoa com o mesmo cpf
    return creted_pessoa



