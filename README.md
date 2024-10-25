---

# CRUD de Usuários com FastAPI e PostgreSQL

Este repositório contém um projeto de API em Python que implementa um CRUD de usuários usando **FastAPI**. A aplicação permite a criação, leitura, atualização e exclusão de usuários, com **Docker** para gestão de containers e **PostgreSQL** como banco de dados relacional.


## 🚀 Funcionalidades da API

A API oferece os seguintes endpoints para manipulação dos dados de usuários:

- **`GET /usuarios`**: Retorna uma lista de todos os usuários.
- **`GET /usuarios/{id}`**: Retorna os dados de um usuário específico.
- **`POST /usuarios`**: Cria um novo usuário.
- **`PUT /usuarios/{id}`**: Atualiza as informações de um usuário.
- **`DELETE /usuarios/{id}`**: Exclui um usuário pelo ID.

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework rápido e moderno para criação de APIs RESTful.
- **SQLAlchemy**: ORM que facilita a manipulação de dados no banco de dados.
- **PostgreSQL**: Banco de dados relacional onde os dados dos usuários são armazenados.
- **Docker**: Gerenciamento de containers para a aplicação e o banco de dados.

## 📦 Configuração e Execução

### Pré-requisitos

Certifique-se de ter **Docker** e **Docker Compose** instalados no seu ambiente.

### Passos para Rodar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Kell22-mkt/Crud_Python_APi.git
    cd Crud_Python_APi
    ```

2. **Configure o Docker Compose** para rodar os containers:
    ```bash
    docker-compose up --build
    ```

3. **Acesse a Documentação**:
   Acesse `http://localhost:8000/docs` para testar a API através da interface 

## 📄 Licença

Este projeto está licenciado sob a licença MIT, permitindo o uso livre e modificações.

---

Este README reflete seu projeto e organiza as informações essenciais para execução e uso da API.
