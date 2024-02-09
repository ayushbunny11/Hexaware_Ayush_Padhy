from abc import ABC, abstractmethod


class IPayrollService(ABC):

    @abstractmethod
    def GeneratePayroll(self, employeeID):
        pass

    @abstractmethod
    def GetPayrollById(self, payrollID):
        pass

    @abstractmethod
    def GetPayrollsForEmployee(self):
        pass

    @abstractmethod
    def GetPayrollsForPeriod(self):
        pass
