import asyncio

import httpx


async def fetch_get(client: httpx.AsyncClient, pokemon_name: str):
    """
    Faz uma requisição assíncrona à PokeAPI para obter informações
    sobre um Pokémon específico.

    Args:
        client (httpx.AsyncClient): Cliente HTTP assíncrono para 
        realizar a requisição.
        pokemon_name (str): Nome do Pokémon a ser buscado.

    Returns:
        None: A função não retorna valores, apenas imprime os
        dados obtidos.

    Raises:
        httpx.HTTPStatusError: Se a requisição falhar com um código de
        status HTTP inválido.
        httpx.RequestError: Se houver um erro de conexão
        durante a requisição.

    O uso de `await` permite que a execução da corrotina pause enquanto 
    aguarda a resposta da API, sem bloquear o restante do programa.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = await client.get(url) # I/O
    data = response.json()
    name = data['name']
    hability = data['moves'][0]['move']
    print(f'name: {name} / move: {hability}')


async def main():
    """
    Função principal que gerencia chamadas assíncronas à API da PokeAPI.

    Funcionamento:
    - Cria um cliente HTTP assíncrono (`httpx.AsyncClient`) dentro de um
    contexto gerenciado (`async with`).
    - Chama `fetch_get(client, 'ditto')` de forma sequencial
    (aguardando a resposta antes de continuar).
    - Usa `asyncio.gather` para buscar informações de múltiplos
    Pokémon **concorretemente**.
    - Imprime "finalizei" após todas as requisições serem concluídas.

    O uso de `asyncio.gather` permite que múltiplas chamadas assíncronas
    ocorram simultaneamente, reduzindo o tempo total de espera
    pelas respostas da API.
    """
    async with httpx.AsyncClient() as client:
        await fetch_get(client, 'ditto') # processo sincrono
        await asyncio.gather(
            fetch_get(client, 'charmander'), # processo assincrono
            fetch_get(client, 'mew'), # processo assincrono
        )
        print('finalizei')
    


asyncio.run(main())
        