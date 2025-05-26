'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''
from abc import ABC, abstractmethod


class VerificarExameInterface(ABC):
    @abstractmethod
    def verificar_condicoes(self) -> bool:
        pass

    @abstractmethod
    def aprovar_exame(self) -> None:
        pass


class AprovaExameSangue(VerificarExameInterface):
    def aprovar_exame(self, exame_tipo: any):
        if self.verificar_condicoes():
            print(f'exame de {exame_tipo} aprovado')

    def verificar_condicoes(self):
        return True


class AprovaExameRaioX(VerificarExameInterface):
    def aprovar_exame(self, exame_tipo: any):
        if self.verificar_condicoes():
            print(f'exame de {exame_tipo} aprovado')

    def verificar_condicoes(self):
        return True


exame_sangue = AprovaExameSangue()
exame_raio_x = AprovaExameRaioX()

exame_sangue.aprovar_exame('Sangue')
exame_raio_x.aprovar_exame('Raio-x')
