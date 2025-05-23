
# EXEMPLO DE UM CÓDIGO MAL FORMATADO COM SUAS RESPONSÁBILIDADES
# class Processo:
#     def executar(self, username: str, password: str) -> None:
#         if isinstance(username, str) and isinstance(password, str):
#             print('Iniciando conexão com base de dados')
#             print('Consultando usuários na base de dados')
#             print('Inserindo novo usuário na base de dados')
#         else:
#             raise Exception('Erro')


# EXEMPLO DE UM CÓDIGO COM SUAS FUNÇÕES BEM SEPARADAS
class Processo:
    def executar(self, username: str, password: str) -> None:
        if self.__verificar_entradas(username, password):
            self.__inicar_conexao_database()
            self.__consultar_usuario_database(username)
            self.__inserir_usuario_database()
        else:
            self.__raise_error('Erro ao verificar entradas')

    def __verificar_entradas(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __inicar_conexao_database(self) -> None:
        print('Iniciando conexão com base de dados')

    def __consultar_usuario_database(self, username: str) -> None:
        print(f'Consultando {username} na base de dados')

    def __inserir_usuario_database(self) -> None:
        print('Inserindo novo usuário na base de dados')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)


processo_instancia = Processo()
processo_instancia.executar('Pedro', '1234')
