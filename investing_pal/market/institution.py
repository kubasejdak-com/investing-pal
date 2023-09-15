from abc import ABC, abstractmethod

from market.account import Account, AccountInfo


class IInstitution(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name: str = name

    def name(self) -> str:
        return self._name

    @abstractmethod
    def get_available_account(self) -> list[AccountInfo]:
        pass

    @abstractmethod
    def open_account(self, account_type: str, name: str) -> Account:
        pass
