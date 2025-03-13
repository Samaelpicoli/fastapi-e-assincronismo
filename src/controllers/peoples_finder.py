"""
Camada de controlador para busca de pessoas.

A classe `PeoplesFinder` contém a lógica de negócio para recuperar os 
dados de pessoas do banco de dados. Ela segue o padrão MVC, onde 
atua como a camada Controller, chamando o repositório e formatando 
os dados antes de retorná-los.

A busca é feita de forma assíncrona para evitar bloqueios na execução.
"""

from src.model.repositories.people_repository import PeopleRepository


class PeoplesFinder:
    """Controlador responsável por buscar dados da tabela 'pessoas'."""

    def __init__(self):
        """
        Inicializa a instância do controlador.

        Cria uma instância do `PeopleRepository`, que será utilizada para 
        recuperar os dados do banco de dados de maneira assíncrona.
        """
        self._peoples_repo = PeopleRepository()

    async def find_people(self) -> dict:
        """
        Retorna a lista de pessoas cadastradas no banco.

        Este método consulta o repositório de pessoas de forma assíncrona,
        garantindo que a execução não seja bloqueada durante a recuperação 
        dos dados.

        Returns:
            dict: Dicionário contendo os dados formatados das pessoas.
        """
        peoples = await self._peoples_repo.get_all_people()  # Busca assíncrona

        formatted_peoples = []
        for people in peoples:
            formatted_peoples.append({'id': people.id, 'name': people.name})

        return {
            'type': "People",
            'count': len(formatted_peoples),
            'attributes': formatted_peoples
        }
