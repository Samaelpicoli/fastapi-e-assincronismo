import asyncio

from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
async def hello_world():
    """
    Rota assíncrona que simula uma operação demorada ao aguardar 20 segundos.

    Funcionamento:
    - `await asyncio.sleep(20)`: Pausa a execução dessa função por 20
    segundos, mas **não bloqueia** a execução do servidor.
    - Como FastAPI suporta async/await, outras requisições podem ser
    processadas enquanto esta está pausada.

    Returns:
        dict: Um dicionário simples como resposta JSON.
    """
    await asyncio.sleep(20)
    return {'hello': 'world'}


if __name__ == '__main__':
    """
    Inicializa o servidor FastAPI com Uvicorn de forma assíncrona.

    - `workers=1`: Usa um único worker assíncrono baseado em `asyncio`.
    - Diferente do Flask (no modo síncrono), FastAPI com Uvicorn permite
    que múltiplas requisições sejam tratadas simultaneamente,
    pois `asyncio.sleep()` não bloqueia a execução.
    - Isso significa que mesmo que uma requisição demore 20 segundos,
    outras podem ser processadas enquanto isso,
    tornando o servidor **mais eficiente**.
    """
    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)