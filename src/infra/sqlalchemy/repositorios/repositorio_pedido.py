from fastapi import HTTPException, status
from typing import List
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido) -> models.Pedido:
        pass

    def buscar_por_id(self, id: int) -> models.Pedido:
        pass

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pass

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pass