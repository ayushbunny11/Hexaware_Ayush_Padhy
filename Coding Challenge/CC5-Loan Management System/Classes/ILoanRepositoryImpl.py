from Loan import Loan
from HomeLoan import HomeLoan
from CarLoan import CarLoan


class ILoanRepositoryImpl:
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def applyLoan(self):
        customerID = int(input("Enter the customerID: "))
        if self.getCustomerById(customerID) is None:
            raise Exception("CustomerNotFoundException")
        principalAmount = float(input("Enter the Principal Amount: "))
        inRate = float(input("Enter the Interest Rate: "))
        loanTerm = int(input("Enter the loan term in 'MONTHS': "))
        loanType = input("Enter the loan type('Car Loan', 'Home Loan', 'Other'). If 'Other', please mention the type "
                         "of loan e.g. 'Example Loan': ")
        loanStatus = "Pending"
        if loanType == "Home Loan":
            propertyAddress = input("Enter the property Address: ")
            propertyValue = float(input("Enter the property Value: "))
            loan = HomeLoan(self.generateUniqueLoanId(), customerID, principalAmount, inRate, loanTerm, loanStatus,
                            propertyAddress, propertyValue)
        elif loanType == "Car Loan":
            carModel = input("Enter the car model: ")
            carValue = float(input("Enter the car Value: "))
            loan = CarLoan(self.generateUniqueLoanId(), customerID, principalAmount, inRate, loanTerm, loanStatus,
                           carModel, carValue)
        else:
            loan = Loan(self.generateUniqueLoanId(), customerID, principalAmount, inRate, loanTerm, loanType,
                        loanStatus)

        confirm = input(print("Your loan ID has been created. Type Yes/No to confirm your Loan Application: "))
        if confirm.upper() == "YES":
            query = "Insert into loan values(%s, %s, %s, %s, %s, %s, %s)"
            values = (loan.loanID, loan.customerID, loan.principalAmount, loan.interestRate, loan.loanTerm,
                      loan.loanStatus, loan.loanType)
            self.dbUtil.executeQuery(query, values)
            return True
        else:
            return False

    def calculateInterest(self, loanID):
        query = "select principalAmount, interestRate, loanTermInMonths from loan where loanID = %s"
        values = (loanID,)
        result = self.dbUtil.fetchOne(query, values)
        if result is None:
            raise Exception("InvalidLoanException")
        pAmount = result[0]
        inRate = result[1]
        term = result[2]
        interest = (pAmount * inRate * term) / 12
        return f"The interest for loanID {loanID} is Rs.{interest}"

    def loanStatus(self, loanID):
        query = "Select creditScore from customer join loan on customer.customerID = loan.customerID and loanID = %s"
        values = (loanID,)
        result = self.dbUtil.fetchOne(query, values)
        creditScore = result[0]
        if creditScore > 650:
            query1 = "update loan set loanStatus='Approved' where loanID=%s"
            values1 = (loanID,)
            self.dbUtil.executeQuery(query1, values1)
            return f"Loan Status Updated to 'Approved' for loanID {loanID}"
        else:
            query1 = "update loan set loanStatus='Rejected' where loanID=%s"
            values1 = (loanID,)
            self.dbUtil.executeQuery(query1, values1)
            return "Your CreditScore is too low. Loan Application Rejected!!!"

    def calculateEMI(self, loanID):
        query = "select principalAmount, interestRate, loanTermInMonths from loan where loanID = %s"
        values = (loanID,)
        result = self.dbUtil.fetchOne(query, values)
        if result is None:
            raise Exception("InvalidLoanException")
        pAmount = result[0]
        inRate = result[1]
        term = result[2]
        # EMI = [P * R * (1+R)^N] / [(1+R)^N-1]
        MIR = (inRate / 12) / 100
        x = (pAmount * MIR * ((1 + MIR) ** term))
        y = ((1 + MIR) ** term - 1)
        emi = x / y
        return f"EMI is calculated to be: {emi}"

    def loanRepayment(self, loanID, amount):
        emi_amt = self.calculateEMI(loanID)
        loanStatus = self.getLoanStatus(loanID)
        if loanStatus == "Approved":
            if amount<emi_amt:
                return f"Payment Rejected!!! Insufficient Amount as per the EMI. Your EMI amount: {emi_amt}"
            else:
                emiCount = amount//emi_amt
                balance = float(self.getPrincipalAmount(loanID)) - float(amount)
                query = "Update loan set principalAmount = %s where loanID=%s"
                values = (balance, loanID)
                self.dbUtil.executeQuery(query, values)
                emiCount -= 1
                return f"Payment Successfull. You can pay the rest in {emiCount} EMI's."
        elif loanStatus == "Pending":
            return f"You loan has not yet been approved. So please wait until its approved."
        else:
            return f"Your Loan has been rejected. Do not make any Payment."

    def getAllLoan(self):
        query = "select * from loan"
        result = self.dbUtil.fetchAll(query)
        for res in result:
            print(res)

    def getLoanById(self, loanID):
        query = "select * from loan where loanID=%s"
        values = (loanID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def get_no_of_loans(self):
        query = "select count(*) from loan"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueLoanId(self):
        return int(self.get_no_of_loans()) + 1

    def getCustomerById(self, customerID):
        query = "select * from customer where customerID = %s"
        values = (customerID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def getLoanStatus(self, loanID):
        query = "select loanStatus from loan where loanID = %s"
        values = (loanID,)
        result = self.dbUtil.fetchOne(query, values)
        return result[0]

    def getPrincipalAmount(self, loanID):
        query = "select principalAmount from loan where loanID = %s"
        values = (loanID,)
        result = self.dbUtil.fetchOne(query, values)
        return result[0]
