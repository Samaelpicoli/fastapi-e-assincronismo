import databases
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import Column, Integer, MetaData, String, Table
import uvicorn


# Definição da URL do banco de dados SQLite
DATABASE_URL = 'sqlite:///./schema.db'

# Criando a instância do banco de dados assíncrono
database = databases.Database(DATABASE_URL)

# Criando metadados do SQLAlchemy
metadata = MetaData()

# Definição da tabela 'pessoas' no banco de dados
PESSOA = Table(
    "pessoas", metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)


async def get_all_people():
    """
    Consulta todas as pessoas no banco de dados de forma assíncrona.

    Retorna:
        list: Lista de registros contendo os nomes das pessoas.
    
    Uso de assincronismo:
        - `await database.fetch_all(query)`: Executa a consulta SQL 
          sem bloquear a execução, permitindo que outras tarefas 
          sejam processadas enquanto a resposta é aguardada.
    """
    query = PESSOA.select()
    result = await database.fetch_all(query)  # Operação de I/O assíncrona
    return result


# Instância da aplicação FastAPI
app = FastAPI()


@app.get('/')
async def read_data():
    """
    Endpoint que busca todas as pessoas no banco de dados.

    Fluxo assíncrono:
        1. Conecta-se ao banco de dados (`await database.connect()`).
        2. Busca todos os registros com `get_all_people()`
        (chamada assíncrona).
        3. Processa os dados e desconecta-se (`await database.disconnect()`).
    
    Retorna:
        JSONResponse: Lista formatada de nomes armazenados no banco.
    """
    await database.connect()  # Conexão assíncrona com o banco de dados
    peoples = await get_all_people()  # Consulta assíncrona ao banco de dados
    print(peoples)

    # Formatando os nomes para a resposta JSON
    formatted_people = [people.name for people in peoples]

    await database.disconnect()  # Desconexão assíncrona do banco de dados
    return JSONResponse(
        content={'pessoas': formatted_people},
        status_code=200
    )


if __name__ == '__main__':
    """
    Inicia o servidor FastAPI com Uvicorn.

    - `workers=1`: Executa o servidor com um único worker assíncrono.
    - FastAPI, combinado com `databases.Database`, permite operações 
      não bloqueantes no banco de dados, melhorando a escalabilidade.
    """
    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)
