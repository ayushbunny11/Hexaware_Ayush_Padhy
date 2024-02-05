from PyCharm.Assignments.BankingSystemFinal.Connection.DBUtil import DBUtil
from PyCharm.Assignments.BankingSystemFinal.Bean.BankServiceProviderImpl import BankServiceProviderImpl
from PyCharm.Assignments.BankingSystemFinal.Bean.CustomerServiceProviderImpl import CustomerServiceProviderImpl



class BankApp:
    def main(self):
        try:
            dbutil = DBUtil(host='localhost', user='root', password='SQL@bunny11', port='3306', database='hmbank')
            bsp = BankServiceProviderImpl(dbutil)
            csp = CustomerServiceProviderImpl(dbutil)
        except Exception as e:
            raise Exception(f"Error Connecting Server: {e}")

        print("Welcome to HMBank App!")
        while True:
            print("What do you want to do?")
            print("1. Create an Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Get Balance")
            print("5. Transfer Money")
            print("6. Get your Account Details")
            print("7. List all Accounts")
            print("8. Get Transaction Details")
            print("9. Get ACCount Type")
            print("10. Exit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                bsp.create_account()
            elif ch == 2:
                accountNum = input("Enter the account number in which you want to deposit:")
                amount = float(input("Enter the amount: "))
                csp.deposit(accountNum, amount)
            elif ch == 3:
                accountNum = input("Enter the account number from which you want to withdraw:")
                amount = float(input("Enter the amount: "))
                csp.withdraw(accountNum, amount)
            elif ch == 4:
                accountNum = input("Enter the account number to get balance:")
                print(csp.get_account_balance(accountNum))
            elif ch == 5:
                fromAcc = input("AccountID of the sender: ")
                toAcc = input("AccountID of the receiver: ")
                amount = float(input("Enter the amount: "))
                csp.transfer(fromAcc, toAcc, amount)
            elif ch == 6:
                accountNum = input("Enter the account number to get details:")
                print(csp.get_AccountDetails(accountNum))
            elif ch == 7:
                bsp.listAccounts()
            elif ch == 8:
                print(csp.getTransactions())
            elif ch == 9:
                accountNum = input("Enter your accountID: ")
                print(csp.getAccountType(accountNum))
            elif ch == 10:
                dbutil.closeConnection()
                break  # Exit the loop


if __name__ == '__main__':
    obj = BankApp()
    obj.main()
