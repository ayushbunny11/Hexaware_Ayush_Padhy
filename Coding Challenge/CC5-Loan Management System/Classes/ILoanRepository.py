from abc import ABC, abstractmethod


class ILoanRepository(ABC):

    @abstractmethod
    def applyLoan(self):
        pass

    @abstractmethod
    def calculateInterest(self, loanID):
        pass

    @abstractmethod
    def loanStatus(self, loanID):
        pass

    @abstractmethod
    def calculateEMI(self, loanID):
        pass

    @abstractmethod
    def loanRepayment(self, loanID, amount):
        pass

    @abstractmethod
    def getAllLoan(self):
        pass

    @abstractmethod
    def getLoanById(self, loanID):
        pass
