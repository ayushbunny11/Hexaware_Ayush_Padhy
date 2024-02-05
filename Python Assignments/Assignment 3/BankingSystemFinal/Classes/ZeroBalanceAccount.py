from PyCharm.Assignments.BankingSystemFinal.Bean.Account import Account


class ZeroBalanceAccount(Account):
    def __init__(self, accountNum):
        super().__init__(accountNum, 'Zero Balance', 0)
        print("Zero Balance Account Activated!!!")



