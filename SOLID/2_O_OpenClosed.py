
# EXEMPLO DE CÓDIGO QUE NÃO SEGUE O PRINCIPIO DE ABERTO E FECHADO
# class Worker:
#     def fazer_trabalho(self, worker: int):
#         if worker == 1:
#             print('Programador está desenvolvendo um sistema')
#         elif worker == 2:
#             print('RH está contratando novos colaboradores')
#         elif worker == 3:
#             print('Vendas está vendendo um novo produto')
#         else:
#             raise Exception('Error, nenhum worker foi encontrado')


# EXEMPLO DE UM CÓDIGO SEGUINDO O CONCEITO ABERTO E FECHADO
# A IDEIA É ACRESCENTAR SEM MODIFICAR A CLASSE WORKER
class Programmer:
    def job(self) -> None:
        print('Programador está desenvolvendo um sistema')


class Rh:
    def job(self) -> None:
        print('RH está contratando novos colaboradores')


class Seller:
    def job(self) -> None:
        print('Vendas está vendendo um novo produto')


class Worker:
    def fazer_trabalho(self, worker: any) -> None:
        worker.job()


trabalho = Worker()

programador = Programmer()
rh = Rh()
vendedor = Seller()

trabalho.fazer_trabalho(programador)
trabalho.fazer_trabalho(rh)
trabalho.fazer_trabalho(vendedor)
