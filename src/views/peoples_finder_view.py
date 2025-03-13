"""
Camada de View para a busca de pessoas.

A classe `PeoplesFinderView` gerencia a interação HTTP no padrão MVC.
Ela atua como a camada de Apresentação, processando requisições e 
formatando respostas antes de enviá-las.

O processo é assíncrono para evitar bloqueios durante a comunicação 
com o controlador.
"""

from typing import Any
from src.controllers.peoples_finder import PeoplesFinder


class PeoplesFinderView:
    """View responsável por processar requisições HTTP relacionadas
    a 'pessoas'."""

    def __init__(self):
        """
        Inicializa a instância da View.

        Cria uma instância do `PeoplesFinder`, que atua como controlador 
        para manipular a lógica de negócio.
        """
        self._controller = PeoplesFinder()

    async def handle_find_people(self, http_request: Any = None) -> dict:
        """
        Manipula a requisição HTTP para buscar pessoas.

        Este método interage com a camada Controller para obter os dados 
        e os formata no padrão HTTP (body + status_code).

        Args:
            http_request (Any, opcional): Objeto da requisição HTTP.

        Returns:
            dict: Dicionário contendo o corpo da resposta e o código HTTP.
        """
        # Chamada assíncrona ao controlador para buscar os dados
        response = await self._controller.find_people()

        # Formatação da resposta HTTP
        http_response = {'body': response, 'status_code': 200}
        return http_response
