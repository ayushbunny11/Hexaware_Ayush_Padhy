from PyCharm.Assignments.BankingSystemFinal.Bean.Account import Account


class CurrentAccount(Account):
    LIMIT = 5000
    def __init__(self, accountNum, balance):
        super().__init__(accountNum, 'Current', balance)
        self.overdraftLimit = self.LIMIT
        print("Current Account Activated!!!")



