from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str

    class Config:
        from_attributes = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        from_attributes = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float

    class Config:
        from_attributes = True

class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
