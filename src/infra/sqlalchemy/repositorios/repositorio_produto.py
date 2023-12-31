from fastapi import HTTPException, status
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id=produto.usuario_id)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos
    
    def buscarPorId(self, id: int):
        produto = self.db.query(models.Produto).filter(models.Produto.id == id).first()
        if produto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
        return produto

    def editar(self, id: int, produto: schemas.Produto):
        update_produto = update(models.Produto). where(
            models.Produto.id == id).values(nome=produto.nome,
                                            detalhes=produto.detalhes,
                                            preco=produto.preco,
                                            disponivel=produto.disponivel)
        self.db.execute(update_produto)
        self.db.commit()
        

    def remover(self, id: int):
        delete_produto = delete(models.Produto).where(
            models.Produto.id == id
        )

        self.db.execute(delete_produto)
        self.db.commit()
