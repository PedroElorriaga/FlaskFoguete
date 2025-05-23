

# EXEMPLO DE CÓDIGO QUE NÃO SEGUE O CONCEITO DE LISKOV
# class Animal:
#     def andar(self):
#         print('O animal esta andando')

#     def comer(self):
#         print('O animal esta comendo')


# class Felino(Animal):
#     def comer(self):
#         print('O felino esta comendo sua raçao')


# EXEMPLO DE CÓDIGO QUE SEGUE O CONCEITO DE LISKOV
# OBJETOS SÃO SUBSTITUIDOS SEM QUE AFETE A VIOLAÇÃO DE SUBSTITUIÇÃO
class Animal:
    # CLASSE GENERICA
    def comer(self):
        print('O animal esta comendo')

    def andar(self):
        print('O animal esta andando')


class Felino(Animal):
    # CLASSE SENTIDO DE HERANÇA
    def atacar(self):
        print('O felino esta atacando')


class Leao(Felino):
    # CLASSE MENOS GENERICA
    def rugir(self):
        print('O leao esta rugindo')


class Observador:
    def observando(self, animal: Animal):
        print('O observador esta vendo...')
        animal.comer()


pessoa = Observador()
leao = Leao()
felino = Felino()
animal = Animal()

# ESTOU MUDANDO UM TIPO POR UM SUBTIPO E O COMPORTAMENTO CONTINUA O MESMO
pessoa.observando(animal)
pessoa.observando(felino)
pessoa.observando(leao)
