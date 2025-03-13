"""
Define o repositório responsável pelas operações da entidade 'Pessoas'.

Este módulo contém a classe `PeopleRepository`, que implementa métodos 
para manipular os dados da tabela 'pessoas'. Ele segue o padrão **Repository** 
para encapsular o acesso ao banco de dados.

A conexão com o banco de dados é gerenciada pelo `DBConnectionHandler`, 
garantindo a execução assíncrona das consultas.
"""

from typing import Any, List
from src.model.entities.peoples import Pessoas
from src.model.settings.db_connection_handler import db_connection_handler


class PeopleRepository:
    """Classe de repositório para operações da tabela 'pessoas'."""

    def __init__(self):
        """
        Inicializa o repositório com a conexão do banco de dados.

        A conexão é obtida de `DBConnectionHandler`, permitindo o uso 
        assíncrono das consultas através do atributo `_conn`.
        """
        self._conn = db_connection_handler.get_db_conn

    async def get_all_people(self) -> List[Any]:
        """
        Retorna todas as pessoas cadastradas no banco.

        Esta operação é assíncrona e utiliza `await` para buscar os dados 
        sem bloquear a execução da aplicação.

        Returns:
            List[Any]: Lista de registros da tabela 'pessoas'.
        """
        query = Pessoas.select()
        result = await self._conn.fetch_all(query)  # Operação assíncrona
        return result
