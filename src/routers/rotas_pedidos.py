from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto


router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pass

@router.get('/pedidos/{id}', status_code=status.HTTP_200_OK, response_model=Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pass

@router.get('/pedidos', status_code=status.HTTP_200_OK, response_model=List[Pedido])
def listar_pedidos(session: Session = Depends(get_db)):
    pass