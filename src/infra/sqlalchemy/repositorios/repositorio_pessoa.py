from sqlalchemy.orm import Session
import infra.sqlalchemy.models.models as models, schemas.schemas as schemas


class RepositorioPessoa():
    def __init__(self, db : Session):
        self.db = db

    def create_pessoa(self, pessoa: schemas.Pessoa):
        # fake_hash = pessoa.cpf + 'alone'
        db_user = models.Pessoa(nome=pessoa.nome,
                                rg=pessoa.rg,
                                cpf=pessoa.cpf,
                                email=pessoa.email,
                                idade=pessoa.idade,
                                formacao=pessoa.formacao,
                                endereco=pessoa.endereco)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
