from abc import ABC, abstractmethod

# EXEMPLO DE CÓDIGO SEM O USO DOS PRINCIPIOS DE INTERFACE SEGRAGATION
# class Document(ABC):
# TODO CLASSE DE INTERFACE GENERICA
#     @abstractmethod
#     def read(self):
#         pass

#     @abstractmethod
#     def write(self):
#         pass

#     @abstractmethod
#     def format(self):
#         pass

#     @abstractmethod
#     def copy(self):
#         pass


# class Pdf(Document):
#     def read(self):
#         print('Lendo documento')

#     def copy(self):
#         print('Copiando dados do PDF')

# TODO FORÇA O USO DE MÉTODOS MESMO SEM UTILIDADE
#     def format(self):
#         print('Sem uso')

#     def write(self):
#         print('Sem uso')


# CÓDIGO USANDO PRINCIPIOS DE INTERFACE SEGREGATION
# SEM INTERFACES USO GENERICAS
class PdfInterface(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def copy(self):
        pass


class TxtInterface(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class CsvInterface(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def format(self):
        pass


class Pdf(PdfInterface):
    def read(self):
        print('Lendo arquivo PDF')

    def copy(self):
        print('Copiando dados do PDF')


arquivo_pdf = Pdf()
arquivo_pdf.read()
arquivo_pdf.copy()
