class Transaction:
    def __init__(self, account, desctiption, dateTime, transactionType, transactionAmount):
        self.account = account
        self.description = desctiption
        self.dateTime = dateTime
        self.transactionType = transactionType
        self.transactionAmount = transactionAmount
        self.type = ("Withdraw", "Deposit", "Transfer")

    def getTransactionDetails(self):
        print("Transaction Details: ")
        print(f"Account ID: {self.account}")
        print(f"Description: {self.description}")
        print(f"Date and Time: {self.dateTime}")
        print(f"Transaction Type: {self.transactionType}")
        print(f"Transaction Amount {self.transactionAmount}")

