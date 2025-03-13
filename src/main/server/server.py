"""
Módulo principal para inicialização do servidor FastAPI.

Este módulo configura a aplicação FastAPI e inclui as rotas 
definidas no módulo `peoples_routes`.

No padrão MVC:
- Esta camada representa a **Interface (View/HTTP)**.
- As rotas são incluídas para lidar com requisições assíncronas.
"""

from fastapi import FastAPI
from src.main.routes.peoples_routes import peoples_routes


# Instância da aplicação FastAPI
app = FastAPI()

# Inclusão das rotas definidas no módulo peoples_routes
app.include_router(peoples_routes)