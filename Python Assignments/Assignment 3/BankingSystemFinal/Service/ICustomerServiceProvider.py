from abc import ABC, abstractmethod


class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, accountNum):
        pass

    @abstractmethod
    def deposit(self, accountNum, amount):
        pass

    @abstractmethod
    def withdraw(self, accountNum, amount):
        pass

    @abstractmethod
    def transfer(self, fromAccountNum, toAccountNum, amount):
        pass

    @abstractmethod
    def get_AccountDetails(self, accountNum):
        pass

    @abstractmethod
    def getTransactions(self):
        pass
