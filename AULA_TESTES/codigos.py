from dataclasses import dataclass
from sqlite3 import Connection


def fizz_buzz(number: int) -> str | int:
    match number % 3 == 0, number % 5 == 0:
        case [True, False]:
            return 'Fizz'
        case [False, True]:
            return 'Buzz'
        case [True, True]:
            return 'FizzBuzz'
        case _:
            return number


# SIMULANDO UM SCHEMA
@dataclass
class CardTask:
    id: int
    tarefa: str
    status: str = 'a fazer'


class CardMutations:
    def __init__(self):
        self.lista_de_tarefas: list[CardTask] = []
        self.id_increment: int = 1

    def create_task(self, tarefa: str, status: str) -> CardTask:
        card = CardTask(self.id_increment, tarefa, status)
        self.lista_de_tarefas.append(card)

        self.id_increment += 1

        return card

    def list_tasks(self) -> list[CardTask]:
        return self.lista_de_tarefas

    def update_task(self, data: dict) -> CardTask | None:
        itens_para_update = ['tarefa', 'status']

        # O(n) -> Nivel Linear
        # tarefa_original = [
        #     tarefa for tarefa in self.lista_de_tarefas if tarefa.id == data['id']]

        # O(1) -> Nivel de constante
        tarefa_original = next(
            (tarefa for tarefa in self.lista_de_tarefas if tarefa.id ==
             data['id']),
            None
        )

        if tarefa_original:
            for item in data:
                if item in itens_para_update:
                    setattr(tarefa_original, item, data[item])

        return tarefa_original


class DataBaseSimulation:
    def __init__(self, conexao_sqlite: Connection) -> None:
        self.cursor = conexao_sqlite.cursor()

    def get_card(self, id: int) -> tuple:
        resultado_da_busca = self.cursor.execute(
            "SELECT * FROM produtos WHERE id=?", (id))
        informacao_do_resultado = resultado_da_busca.fetchone()

        return informacao_do_resultado


def api_simulation(cep):
    import requests

    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if resposta.status_code == 200:
        return resposta.json()
    return None
