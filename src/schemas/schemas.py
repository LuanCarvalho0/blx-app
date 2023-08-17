from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float

    class Config:
        from_attributes = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str

    produtos: List[ProdutoSimples] = []

    class Config:
        from_attributes = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        from_attributes = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int] = None
    usuario: Optional[UsuarioSimples] = None

    class Config:
        from_attributes = True

class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str] = None
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'

    usuario_id: Optional[int] = None
    produto_id: Optional[int] = None

    usuario: Optional[UsuarioSimples] = None
    produto: Optional[ProdutoSimples] = None

    class Config:
        from_attributes = True