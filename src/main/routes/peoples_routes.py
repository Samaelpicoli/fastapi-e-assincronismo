"""
Módulo responsável por definir as rotas HTTP relacionadas a pessoas.

Este módulo segue o padrão **MVC**, onde:
- Representa a **Camada de Roteamento (View/Interface HTTP)**.
- Recebe requisições HTTP, repassa para a camada de **Controle** 
  e retorna respostas formatadas.

Uso do FastAPI:
- O `APIRouter` é utilizado para modularizar as rotas.
- As chamadas ao banco de dados ocorrem de forma **assíncrona**,
  evitando bloqueios durante requisições concorrentes.
"""

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.model.settings.db_connection_handler import db_connection_handler
from src.views.peoples_finder_view import PeoplesFinderView


# Instância do roteador para endpoints relacionados a "peoples"
peoples_routes = APIRouter()


@peoples_routes.get('/peoples')
async def get_peoples(request: Request):
    """
    Rota para buscar todas as pessoas cadastradas no banco de dados.

    Fluxo assíncrono:
    1. Conecta-se ao banco de dados.
    2. Chama o **Controller** para processar os dados.
    3. Desconecta-se do banco de dados.
    4. Retorna a resposta formatada como JSON.

    Args:
        request (Request): Objeto da requisição HTTP.

    Returns:
        JSONResponse: Resposta HTTP contendo os dados das pessoas.
    """
    peoples_finder_view = PeoplesFinderView()

    # Conexão assíncrona com o banco de dados
    await db_connection_handler.connect_to_db()

    # Processa a busca das pessoas via controller
    http_response = await peoples_finder_view.handle_find_people()

    # Fecha a conexão com o banco de dados após a requisição
    await db_connection_handler.disconnect_to_db()

    # Retorna a resposta formatada
    return JSONResponse(
        content=http_response['body'],
        status_code=http_response['status_code']
    )
