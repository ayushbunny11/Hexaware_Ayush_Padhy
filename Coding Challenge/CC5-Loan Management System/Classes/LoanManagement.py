from DBUtil import DBUtil
from ILoanRepositoryImpl import ILoanRepositoryImpl


class LoanManagement:
    def main(self):
        dbUtil = DBUtil(host='localhost', user='root', password='SQL@bunny11', port=3306, database='lmsystem')
        lrs = ILoanRepositoryImpl(dbUtil)

        print("Welcome to the LOAN MANAGEMENT APP.")
        while True:
            print("What do you want to do?")
            print("1. Apply Loan")
            print("2. Get All Loans")
            print("3. Get Your Loan")
            print("4. Repay Your Loan")
            print("5. Check Your Loan Status")
            print("6. Update Your Loan Status")
            print("7. Calculate the Interest on your Loan")
            print("8. Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                result = lrs.applyLoan()
                if result:
                    print("Loan Applied")
                else:
                    print("Loan Application Cancelled")
            elif ch == 2:
                lrs.getAllLoan()
            elif ch == 3:
                loanID = int(input("Enter your loan ID: "))
                result = lrs.getLoanById(loanID)
                if result is None:
                    print("Invalid Loan ID!!!")
                else:
                    print(result)
            elif ch == 4:
                loanID = int(input("Enter your loan ID: "))
                amount = float(input("Enter the amount to repay: "))
                print(lrs.loanRepayment(loanID, amount))
            elif ch == 5:
                loanID = int(input("Enter your loan ID: "))
                print(lrs.getLoanStatus(loanID))
            elif ch == 6:
                loanID = int(input("Enter your loan ID: "))
                print(lrs.loanStatus(loanID))
            elif ch == 7:
                loanID = int(input("Enter your loan ID: "))
                print(lrs.calculateInterest(loanID))
            else:
                dbUtil.closeConnection()
                break


if __name__ == '__main__':
    obj = LoanManagement()
    obj.main()
