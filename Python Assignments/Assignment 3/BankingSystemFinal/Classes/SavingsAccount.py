from PyCharm.Assignments.BankingSystemFinal.Bean.Account import Account


class SavingsAccount(Account):
    def __init__(self, accountNum):
        super().__init__(accountNum, 'Savings', 500)
        self.interestRate = 4.5
        print("Savings Account Activated!!!")

    def calculateInterest(self):
        interest = self.balance * (self.interestRate / 100)
        self.balance += interest
        print(f"After {interest} Interest, account balance is: {self.balance}")


