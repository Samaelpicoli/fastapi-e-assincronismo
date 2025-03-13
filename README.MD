# 📌 Projeto de Estudo - Assincronismo com FastAPI

Este repositório contém um projeto de estudo sobre assincronismo em Python,
inspirado na [playlist do Programador Lhama](https://www.youtube.com/playlist?list=PLAgbpJQADBGJserIipQ04-bZjRrqjvJmV).
O projeto é desenvolvido utilizando o framework **FastAPI** e segue o padrão arquitetural **MVC**.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **FastAPI** (Framework web assíncrono)
- **Uvicorn** (Servidor ASGI)
- **SQLAlchemy** (ORM para manipulação do banco de dados)
- **Databases** (Abstração assíncrona para conexão com banco de dados)
- **SQLite** (Banco de dados leve para testes e estudos)

---

## 📂 Estrutura do Código

O projeto segue o padrão **MVC (Model-View-Controller)**, dividido da seguinte forma:

### **1. Model (Camada de Dados)**
- **`model/entities/peoples.py`**: Define a entidade/tabela "Pessoas" usando SQLAlchemy.
- **`model/repositories/people_repository.py`**: Responsável pela interação com o banco de dados.
- **`model/settings/db_connection_handler.py`**: Gerencia a conexão assíncrona com o banco de dados.
- **`model/settings/db_metadata.py`**: Define os metadados do banco de dados.

### **2. Controller (Regra de Negócio)**
- **`controllers/peoples_finder.py`**: Contém a lógica para buscar pessoas no banco e formatar os dados.

### **3. View (Interação com HTTP)**
- **`views/peoples_finder_view.py`**: Controla as requisições HTTP, validando e formatando respostas.

### **4. Server e Rotas**
- **`main/server/server.py`**: Inicializa o FastAPI e inclui as rotas.
- **`main/routes/people_routes.py`**: Define as rotas HTTP e conecta com as views.

---

## ▶️ Como Executar o Projeto

### Criar e Ativar um Ambiente Virtual**
```bash
python -m venv venv  # Cria o ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### Instalar as Dependências**
```bash
pip install -r requirements.txt
```

### Executar o Servidor**
```bash
python run.py
```

O servidor iniciará em [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

---

## 📌 Endpoints Disponíveis

- **`GET /peoples`** → Retorna a lista de pessoas cadastradas.

Exemplo de resposta:
```json
{
  "type": "People",
  "count": 2,
  "attributes": [
    { "id": 1, "name": "João" },
    { "id": 2, "name": "Maria" }
  ]
}
```



