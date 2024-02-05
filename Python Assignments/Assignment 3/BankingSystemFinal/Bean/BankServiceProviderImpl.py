from PyCharm.Assignments.BankingSystemFinal.Service.IBankServiceProvider import IBankServiceProvider


class BankServiceProviderImpl(IBankServiceProvider):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def create_account(self):
        customerID = input("Please enter your customerID: ")
        if self.existingCustomer(customerID) is None:
            raise Exception("CustomerNotRegisteredException")
        else:
            print("Please fill up the account details: ")
            account = {
                'accountID': self.generateUniqueAccountID(),
                'customerID': customerID,
            }
            print("What type of account do you want to create?")
            print("1. Savings Account")
            print("2. Current Account")
            print("3. Zero Balance Account")
            ch = int(input("Enter your choice: "))

            match ch:
                case 1:
                    account['account_type'] = 'savings'
                    account['balance'] = float(input("Enter the amount: "))
                    return self.AddAccountIntoDatabase(account)

                case 2:
                    account['account_type'] = 'current'
                    account['balance'] = float(input("Enter the amount: "))
                    return self.AddAccountIntoDatabase(account)

                case 3:
                    account['account_type'] = 'zero balance'
                    account['balance'] = 0.0
                    return self.AddAccountIntoDatabase(account)

    def listAccounts(self):
        query = "SELECT accountID, customerID, account_type, balance FROM accounts"
        result = self.dbUtil.fetchall(query, values=None)
        print(result)

    def get_AccountDetails(self, accountNum):
        query = "Select * from accounts where accountID=(%s)"
        value = (accountNum,)
        return self.dbUtil.fetchall(query, value)

    def calculateInterest(self, inRate=4.5):
        query = "select balance * %s as inRate from accounts"
        return self.dbUtil.fetchall(query, inRate)

    def get_no_of_accounts(self):
        query = "Select count(*) from accounts"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueAccountID(self):
        concat = ('B0', str(self.get_no_of_accounts()+ 1))
        return "".join(concat)

    def existingCustomer(self, customerID):
        query = "Select * from Customers where customerID = %s"
        value = (customerID,)
        return self.dbUtil.fetchOne(query, value)

    def AddAccountIntoDatabase(self, accounts):
        query = "insert into accounts values(%s, %s, %s, %s)"
        values = (accounts['accountID'], accounts['customerID'], accounts['account_type'], accounts['balance'])
        return self.dbUtil.executeQuery(query, values)
