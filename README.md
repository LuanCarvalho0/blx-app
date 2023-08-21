# BLX-App: Aplicativo de Compra e Venda Inspirado na OLX

Bem-vindo ao repositório do BLX-App! Este é um aplicativo desenvolvido em Python com o framework FASTAPI, utilizando SQLite como banco de dados e Alembic para migrações. O aplicativo é uma plataforma de compra e venda, similar à OLX, onde os usuários podem se cadastrar, cadastrar produtos para venda e fazer pedidos de produtos de outros usuários. A autenticação de usuários é realizada através do JWT (JSON Web Token).

## Funcionalidades Principais

O BLX-App oferece as seguintes funcionalidades principais:

1. **Cadastro e Autenticação de Usuários:** Os usuários podem se registrar no aplicativo, fornecendo informações como nome, telefone e senha. A autenticação é feita através de tokens JWT, proporcionando segurança durante as interações.

2. **Cadastro de Produtos:** Os usuários podem cadastrar produtos para venda. Eles podem adicionar nome, detalhes, preco, disponivel e usuario_id dos produtos. Cada produto é associado ao usuário que o cadastrou.

3. **Listagem de Produtos:** Os produtos cadastrados são exibidos em uma lista, permitindo que os usuários naveguem pelos itens disponíveis para compra.

4. **Pedidos de Produtos:** Os usuários podem fazer pedidos para comprar produtos de outros usuários.
## Requisitos de Instalação

Certifique-se de ter Python 3.x instalado. Para configurar o ambiente do BLX-App, siga os passos abaixo:

1. Clone este repositório:

   ```
   git clone https://github.com/LuanCarvalho0/blx-app
   ```

2. Crie um ambiente virtual (recomendado) e ative-o:

   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:

   ```
   alembic upgrade head
   ```

5. Execute o aplicativo:

   ```
   uvicorn src.server:app --reload
   ```

O aplicativo estará disponível em `http://localhost:8000`.

## Contribuição

Contribuições são bem-vindas! Se você deseja adicionar novas funcionalidades, corrigir bugs ou melhorar a documentação, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
