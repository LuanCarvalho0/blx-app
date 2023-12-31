from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.routers.auth_utils import obter_usuario_logado
from src.schemas.schemas import Pedido, Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido


router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}', status_code=status.HTTP_200_OK, response_model=Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pedido = RepositorioPedido(session).buscar_por_id(id)
    return pedido

@router.get('/pedidos', status_code=status.HTTP_200_OK, response_model=List[Pedido])
def listar_pedidos(usuario: Usuario = Depends(obter_usuario_logado), 
                   session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_meus_pedidos_por_usuario_id(usuario.id)
    return pedidos

@router.get('/pedidos/{usuario_id}/vendas', status_code=status.HTTP_200_OK, response_model=List[Pedido])
def listar_vendas(usuario_id: int, session: Session = Depends(get_db)):
    vendas = RepositorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return vendas