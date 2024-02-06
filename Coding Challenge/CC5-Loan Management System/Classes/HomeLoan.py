from Loan import Loan


class HomeLoan(Loan):
    def __init__(self, loanID, customerID, principalAmount, interestRate, loanTerm, loanStatus, propertyAddress,
                 propertyValue):
        super().__init__(loanID, customerID, principalAmount, interestRate, loanTerm, "Home Loan", loanStatus)
        self.propertyAddress = propertyAddress
        self.propertyValue = propertyValue

    @property
    def propertyAddress(self):
        return self.propertyAddress

    @property
    def propertyValue(self):
        return self.propertyValue

    @propertyAddress.setter
    def propertyAddress(self, propertyAddress):
        self.propertyAddress = propertyAddress

    @propertyValue.setter
    def propertyValue(self, propertyValue):
        self.propertyValue = propertyValue
