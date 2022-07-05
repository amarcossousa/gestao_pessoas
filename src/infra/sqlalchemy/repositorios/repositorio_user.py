from sqlalchemy.orm import Session
from schemas.schema import User

class RepositorioUser():
    def __init__(self, db : Session):
        self.db = db

    def create_user(self, user: User):
        # fake_hash = pessoa.cpf + 'alone'
        db_user = User(email=user.email,
                        cpf=user.cpf,
                        senha=user.senha)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
