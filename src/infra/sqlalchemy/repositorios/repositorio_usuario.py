from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: schemas.Usuario):
        usuario_bd = models.Usuario(nome=usuario.nome,
                                    telefone=usuario.telefone,
                                    senha=usuario.senha)
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd


    def listar(self):
        usuarios = self.session.query(models.Usuario).all()
        return usuarios

    def obter_por_telefone(self, telefone):
        usuario = self.session.query(models.Usuario).where(
            models.Usuario.telefone == telefone
        ).first()
        return usuario
