from sqlalchemy import Column, String, Integer, Boolean
from infra.sqlalchemy.config.database import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column (Integer, primary_key=True)
    nome = Column (String)
    rg = Column (String)
    cpf= Column (String)
    email = Column (String)
    idade = Column (Integer)
    formacao = Column (String)
    endereco = Column (String)
    admin = Column (Boolean)