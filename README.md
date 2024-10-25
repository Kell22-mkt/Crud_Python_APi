Aqui está uma versão mais concisa e direta do README para o seu projeto de CRUD de usuários:

---

# Desafio Técnico: CRUD de Usuários com FastAPI e PostgreSQL

Este projeto é uma API desenvolvida com **FastAPI** que implementa um CRUD completo para gerenciar usuários. A aplicação é executada em containers Docker e utiliza **PostgreSQL** como banco de dados, com **SQLAlchemy** para interagir com os dados de forma eficiente.

## 📌 Funcionalidades da API

A API oferece os seguintes endpoints:

- **`GET /usuarios`**: Lista todos os usuários.
- **`GET /usuarios/{id}`**: Detalhes de um usuário específico.
- **`POST /usuarios`**: Criação de um novo usuário.
- **`PUT /usuarios/{id}`**: Atualização dos dados de um usuário.
- **`DELETE /usuarios/{id}`**: Remoção de um usuário pelo ID.

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework moderno para construção de APIs.
- **SQLAlchemy**: ORM para Python, facilitando a interação com o banco de dados.
- **PostgreSQL**: Banco de dados relacional.
- **Docker**: Isolamento e gestão de ambientes para aplicação e banco de dados.

## 🛠️ Configuração e Execução

1. **Clone o repositório** e navegue até a pasta do projeto:
    ```bash
    git clone https://github.com/seuusuario/repositorio.git
    cd repositorio
    ```

2. **Inicie o Docker Compose**:
    ```bash
    docker-compose up --build
    ```

3. **Testar a API**: Acesse a documentação automática em `http://localhost:8000/docs`.

## 🐳 Docker Compose

O projeto é configurado para rodar em dois containers:
- **db**: Container para o banco de dados PostgreSQL.
- **web**: Container para a aplicação FastAPI.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e modificar conforme necessário.

---

Esse README resume bem o projeto e fornece as instruções essenciais para execução e testes.
