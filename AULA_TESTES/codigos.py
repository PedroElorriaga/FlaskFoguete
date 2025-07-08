from dataclasses import dataclass


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
