from unittest.mock import Mock


# Simula um objeto cursor do SQLite
class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock(return_value=self)
        self.fetchone = Mock()
        self.lastrowid = Mock()
        '''
        Ou seja, quando no seu código você chama cursor.execute(...) ou 
        cursor.fetchone(), ele não faz nada real, mas você pode definir o que ele 
        vai retornar ou verificar se foi chamado.
        '''


# Simula o objeto de conexão do SQLite
class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()
