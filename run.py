# TODO: VER AULA 10 NOVAMENTE PARA ANOTAÇÕES


"""
Módulo responsável por iniciar a aplicação FastAPI.

Este script executa o servidor **Uvicorn**, que é um servidor ASGI 
assíncrono e eficiente para rodar aplicações FastAPI.

Fluxo:
1. O servidor **importa e executa** a aplicação FastAPI definida em 
   `src.main.server.server:app`.
2. A aplicação fica disponível na porta `8000` e aceita conexões de 
   qualquer IP (`0.0.0.0`), permitindo acesso externo.

Por ser uma aplicação **assíncrona**, o Uvicorn permite múltiplas 
requisições simultâneas, otimizando o desempenho da API.
"""

import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'src.main.server.server:app',
        host='0.0.0.0',
        port=8000
    )