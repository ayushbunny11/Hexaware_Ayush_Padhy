import email

from PyCharm.Assignments.BankingSystemFinal.Classes.Customer import Customer
from PyCharm.Concepts.Literals import address


class Account(Customer):
    def __init__(self, account_num: int, account_type: str, balance: float, lastAccNo=None, customerID=None,
                 lastName=None, email=None, firstName=None, phone=None):
        super().__init__(customerID, firstName, lastName, email, phone, address)
        self.account_num = account_num
        self.account_type = account_type
        self.balance = balance
        self.lastAccNo = lastAccNo

    @property
    def accountNum(self):
        return self.account_num

    @property
    def accountType(self):
        return self.account_type

    @property
    def balance(self):
        return self.balance

    @property
    def lastAccNo(self):
        return self.lastAccNo

    @accountNum.setter
    def accountNum(self, accountNum):
        self.account_num = accountNum

    @accountType.setter
    def accountType(self, type):
        self.account_type = type

    @balance.setter
    def balance(self, bal):
        self.balance = bal

    @lastAccNo.setter
    def lastAccNo(self, lastAccNo):
        self.lastAccNo = lastAccNo

    def getAccountDetails(self):
        print("Account Details: ")
        print(f"Account Number: {self.account_num}")
        print(f"Account Type: {self.account_type}")
        print(f"Customer ID: {self.customerID}")
        print(f"Customer Name: {self.firstName} {self.lastName}")
        print(f"Balance: {self.balance}")

    def depositAmount(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "Invalid"

    def withdrawAmount(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return self.balance

    # def calculateInterest(self):
    #     interest = self.balance * (self.in_rate / 100)
    #     self.balance += interest
    #     print(f"After {interest} Interest, account balance is: {self.balance}")
