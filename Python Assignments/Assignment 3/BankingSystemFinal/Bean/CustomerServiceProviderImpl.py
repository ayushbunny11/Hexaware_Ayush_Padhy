from PyCharm.Assignments.BankingSystemFinal.Service.ICustomerServiceProvider import ICustomerServiceProvider
from PyCharm.Assignments.BankingSystemFinal.Classes.CurrentAccount import CurrentAccount


class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def get_account_balance(self, accountNum):
        query = "Select balance from accounts where accountID = %s"
        value = (accountNum,)
        result = self.dbUtil.fetchOne(query, value)
        return result[0]

    def deposit(self, accountNum, amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            if self.get_AccountDetails(accountNum) is not None:
                balance = self.get_account_balance(accountNum)
                newBal = float(balance) + amount
                query = "Update accounts set balance=%s where accountID = %s"
                values = (newBal, accountNum)
                self.dbUtil.executeQuery(query, values)
                print(f"New Balance is: {newBal}")
            else:
                raise Exception("InvalidAccountIDException")

    def withdraw(self, accountNum, amount):
        currentBal = self.get_account_balance(accountNum)
        accountType = self.getAccountType(accountNum)

        if self.get_AccountDetails(accountNum) is not None:
            if amount <= 0:
                return "Invalid Amount"
            else:
                if accountType == 'savings':
                    if amount > currentBal:
                        raise Exception("InsufficientFundException")
                    else:
                        if float(currentBal) - amount < 500.00:
                            raise Exception("MinimumBalanceLimitException")
                        else:
                            query = "Update accounts set balance=balance-%s where accountID = %s"
                            values = (amount, accountNum)
                            self.dbUtil.executeQuery(query, values)
                            result = self.get_account_balance(accountNum)
                            return result
                elif accountType == 'current':
                    if amount > currentBal and amount - currentBal > CurrentAccount.LIMIT:
                        raise Exception("OverdraftLimitExceededException")
                    else:
                        query = "Update accounts set balance=balance-%s where accountID = %s"
                        values = (amount, accountNum)
                        self.dbUtil.executeQuery(query, values)
                        result = self.get_account_balance(accountNum)
                        return result
                else:
                    raise Exception("ZeroBalanceAccountException")
        else:
            raise Exception("InvalidAccountIDException")

    def transfer(self, fromAccountNum, toAccountNum, amount):
        if self.get_AccountDetails(fromAccountNum) and self.get_AccountDetails(toAccountNum):
            try:
                self.withdraw(fromAccountNum, amount)
                self.deposit(toAccountNum, amount)
            except Exception as e:
                return f"Transfer Failed!!! Error: {e}"

    def get_AccountDetails(self, accountNum):
        query = "Select * from accounts join customers on accounts.customerID = customers.customerID where accountID=%s"
        value = (accountNum,)
        result = self.dbUtil.fetchall(query, value)
        return result

    def getTransactions(self):
        accountNum = input("Enter your accountID: ")
        fromDate = input("From: ")
        toDate = input("To: ")
        if self.get_AccountDetails(accountNum) is not None:
            query = "Select * from transactions where transaction_date between %s and %s and accountID = %s"
            values = (fromDate, toDate, accountNum)
            result = self.dbUtil.fetchall(query, values)
            return result
        else:
            raise Exception("InvalidAccountIDException")

    def getAccountType(self, accountNum):
        value = (accountNum,)
        result = self.dbUtil.fetchOne("Select account_type from accounts where accountID = %s", value)
        return result[0]
