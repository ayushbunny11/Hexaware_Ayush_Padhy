from abc import ABC, abstractmethod


class ITaxService(ABC):

    @abstractmethod
    def CalculateTax(self):
        pass

    @abstractmethod
    def GetTaxById(self, taxID):
        pass

    @abstractmethod
    def GetTaxesForEmployee(self, employeeID):
        pass

    @abstractmethod
    def GetTaxesForYear(self, taxYear):
        pass

