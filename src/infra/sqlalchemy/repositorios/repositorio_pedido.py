from fastapi import HTTPException, status
from typing import List
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido):
        pedido_db = models.Pedido(quantidade=pedido.quantidade,
                                  local_entrega=pedido.local_entrega,
                                  tipo_entrega=pedido.tipo_entrega,
                                  observacao=pedido.observacao,
                                  usuario_id=pedido.usuario_id,
                                  produto_id=pedido.produto_id)
        
        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)
        return pedido_db

    def buscar_por_id(self, id: int):
        pedido = self.session.query(models.Pedido).filter(models.Pedido.id == id).first()
        if pedido is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado")
        return pedido

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pedidos = self.session.query(models.Pedido).filter(models.Pedido.usuario_id == usuario_id).all()
        if pedidos is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado")
        return pedidos

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        vendas = self.session.query(models.Pedido).join(models.Usuario, models.Usuario.id == models.Pedido.usuario_id).filter(models.Usuario.id == usuario_id).all()
        return vendas