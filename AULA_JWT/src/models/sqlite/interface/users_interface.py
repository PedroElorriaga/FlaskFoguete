from abc import ABC, abstractmethod
from typing import Optional, List


class UsersInterface(ABC):
    @abstractmethod
    def insert_data(self, nome_usuario: str, agencia: int, conta: int, saldo: float, email: str, senha: str) -> bool:
        pass

    @abstractmethod
    def search_data(self, id: Optional[int] = None, nome_usuario: Optional[str] = None, email: Optional[str] = None) -> tuple:
        pass

    @abstractmethod
    def search_all_datas(self) -> List[tuple]:
        pass
