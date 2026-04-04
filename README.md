# Luiza Labs + Dio - APIs assíncronas com FastAPI 

# 🚀 Dio Blog API (FastAPI)

<p align="center">
  <img src="https://assets.dio.me/6EpPMEkR_2cT8ag7Pu4nWmHKuJmsUBfn-ywSo8S3yhI/f:webp/q:80/w:480/L3RyYWNrcy84MmI1NWE0OC1kOTlmLTRjZDItYjJhMC1hNjc0N2JkYjM5YzUucG5n" alt="FastAPI Logo" width="300">
</p>

Uma API assíncrona para gerenciamento de posts de blog, desenvolvida com **FastAPI**, **SQLAlchemy Core** e **Databases**. O projeto utiliza **Poetry** para gerenciamento de dependências e **JWT** para autenticação segura.

---

## 🛠️ Tecnologias e Versões
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1280px-Python-logo-notext.svg.png" alt="Python" height="70">
  &nbsp;&nbsp;
  <img src="https://avatars.githubusercontent.com/u/156354296?s=280&v=4" alt="FastAPI" height="70">
  &nbsp;&nbsp;
  <img src="https://avatars.githubusercontent.com/u/48722593?s=200&v=4" alt="Poetry" height="70">
  &nbsp;&nbsp;
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYgKRIQVJKBIb7E_xXvu49YoGeZNb_88ImEQ&s" alt="SQLite" height="70">
</p>
---

## ⚙️ Instalação e Configuração

Certifique-se de ter o **Python 3.13+** instalado.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/cristiano-muroni/dio-luizalabs-api-assincrona-com-fastapi
   cd dio-blog

2. **Instale as depêndencias com Poetry**
    ```bash
    poetry install

## 🏃 Como Executar
    ```bash
    poetry run uvicorn main:app --reload

 Acesse a documentação interativa da API em:
 👉 127.0.0

🔒 Autenticação JWT
A API protege rotas sensíveis (Create, Update, Delete) através de tokens.
Use a rota /auth/login para obter seu access_token.
No Swagger (/docs), clique no botão Authorize.

📁 Estrutura do Código
```text
dio-blog/
├── main.py            # Ponto de entrada e Lifespan
├── database.py        # Conexão assíncrona e Metadata
├── security.py        # Lógica de tokens JWT
├── models/            # Tabelas SQLAlchemy
├── schemas/           # Validação Pydantic (Entrada)
├── views/             # Modelos de Resposta (Saída)
├── services/          # Regras de negócio (CRUD)
└── controllers/       # Endpoints da API
```



