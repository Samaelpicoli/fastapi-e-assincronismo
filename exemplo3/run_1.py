import time

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Rota síncrona que simula uma operação demorada ao aguardar 30 segundos.

    Funcionamento:
    - `time.sleep(30)`: Bloqueia a thread principal por 30 segundos
    antes de retornar a resposta.
    - Como Flask é síncrono por padrão, enquanto essa requisição está
    sendo processada, nenhuma outra requisição pode ser atendida
    (a menos que `threaded=True` seja usado no `app.run`).

    Returns:
        dict: Um dicionário simples como resposta JSON.
    """
    time.sleep(30)
    return {'Hello': 'World'}


if __name__ == '__main__':
    """
    Inicializa o servidor Flask de forma síncrona.

    - `threaded=False`: O servidor usará uma única thread,
    o que significa que apenas **uma requisição** será processada por vez.
    Se várias requisições forem recebidas, elas ficarão na fila até que
    a anterior seja concluída.
    - Flask, por padrão, roda de forma **bloqueante**, tornando-o menos
    eficiente para operações demoradas.
    """
    app.run(host='0.0.0.0', port=8000, threaded=False)