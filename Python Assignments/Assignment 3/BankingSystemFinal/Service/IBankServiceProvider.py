from abc import ABC, abstractmethod


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def listAccounts(self):
        pass

    @abstractmethod
    def get_AccountDetails(self, accountNum):
        pass

    @abstractmethod
    def calculateInterest(self, inRate):
        pass
