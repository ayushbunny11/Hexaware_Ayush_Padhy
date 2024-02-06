class Loan:
    def __init__(self, loanID, customerID, principalAmount, interestRate, loanTerm, loanType, loanStatus):
        self.loanID = loanID
        self.customerID = customerID
        self.principalAmount = principalAmount
        self.interestRate = interestRate
        self.loanTerm = loanTerm
        self.loanType = loanType
        self.loanStatus = loanStatus

    @property
    def loanID(self):
        return self.loanID

    @property
    def principalAmount(self):
        return self.principalAmount

    @property
    def interestRate(self):
        return self.interestRate

    @property
    def loanTerm(self):
        return self.loanTerm

    @property
    def loanType(self):
        return self.loanType

    @property
    def loanStatus(self):
        return self.loanStatus

    @loanID.setter
    def loanID(self, loanID):
        self.loanID = loanID

    @principalAmount.setter
    def principalAmount(self, principalAmount):
        self.principalAmount = principalAmount

    @interestRate.setter
    def interestRate(self, interestRate):
        self.interestRate = interestRate

    @loanTerm.setter
    def loanTerm(self, loanTerm):
        self.loanTerm = loanTerm

    @loanType.setter
    def loanType(self, loanType):
        self.loanType = loanType

    @loanStatus.setter
    def loanStatus(self, loanStatus):
        self.loanStatus = loanStatus

