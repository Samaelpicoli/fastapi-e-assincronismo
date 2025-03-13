"""
Gerencia a conexão assíncrona com o banco de dados.

A classe `DBConnectionHandler` encapsula a lógica de conexão e 
desconexão do banco, garantindo que todas as operações sigam o 
padrão assíncrono para evitar bloqueios.
"""

from databases import Database


class DBConnectionHandler:
    """Manipulador da conexão com o banco de dados."""

    def __init__(self):
        """
        Inicializa o manipulador de conexão.

        Define a URL do banco e cria uma instância da classe `Database`,
        que permite operações assíncronas sobre a conexão.
        """
        self._connection_string = 'sqlite:///./schema.db'
        self._database = Database(self._connection_string)

    async def connect_to_db(self):
        """
        Estabelece a conexão assíncrona com o banco de dados.

        O método `await connect()` permite iniciar a conexão de forma não 
        bloqueante, evitando travamentos na aplicação.
        """
        await self._database.connect()

    async def disconnect_to_db(self):
        """
        Fecha a conexão assíncrona com o banco de dados.

        O método `await disconnect()` garante que a conexão seja fechada 
        corretamente ao final das operações.
        """
        await self._database.disconnect()

    @property
    def get_db_conn(self):
        """
        Retorna a instância da conexão com o banco de dados.

        Isso permite que os repositórios acessem a conexão sem a necessidade 
        de instanciar diretamente o `Database`, mantendo o encapsulamento.
        """
        return self._database


db_connection_handler = DBConnectionHandler()  # Instância única do handler
