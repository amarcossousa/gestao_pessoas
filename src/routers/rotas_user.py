from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.schema import User
from infra.sqlalchemy.repositorios.repositorio_user import RepositorioUser
from infra.sqlalchemy.config.database import get_db



router = APIRouter()

@router.post("/user/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    creted_user = RepositorioUser(db).create_user(user)
    # Incluir excessão para não permitir inserir pessoa com o mesmo cpf
    return creted_user