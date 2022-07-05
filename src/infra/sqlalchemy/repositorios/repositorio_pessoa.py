from sqlalchemy.orm import Session
from schemas.schema import Pessoa


class RepositorioPessoa():
    def __init__(self, db : Session):
        self.db = db

    def create_pessoa(self, pessoa: Pessoa):
        # fake_hash = pessoa.cpf + 'alone'
        db_pessoa = Pessoa(nome=pessoa.nome,
                            rg=pessoa.rg,
                            cpf=pessoa.cpf,
                            email=pessoa.email,
                            idade=pessoa.idade,
                            formacao=pessoa.formacao,
                            endereco=pessoa.endereco)
        self.db.add(db_pessoa)
        self.db.commit()
        self.db.refresh(db_pessoa)
        return db_pessoa
