from abc import ABC, abstractmethod
from typing import Optional


class UsersInterface(ABC):
    @abstractmethod
    def insert_data(self, nome_usuario: str, agencia: int, conta: int, email: str, senha: str) -> bool:
        pass

    @abstractmethod
    def search_data(self, id: Optional[int] = None, nome_usuario: Optional[str] = None, email: Optional[str] = None) -> tuple:
        pass
