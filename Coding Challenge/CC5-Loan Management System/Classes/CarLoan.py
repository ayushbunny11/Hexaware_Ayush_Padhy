from Loan import Loan


class CarLoan(Loan):
    def __init__(self, loanID, customerID, principalAmount, interestRate, loanTerm, loanStatus, carModel,
                 carValue):
        super().__init__(loanID, customerID, principalAmount, interestRate, loanTerm, "Car Loan", loanStatus)
        self.carModel = carModel
        self.carValue = carValue

    @property
    def carModel(self):
        return self.carModel

    @property
    def carValue(self):
        return self.carValue

    @carModel.setter
    def carModel(self, carModel):
        self.carModel = carModel

    @carValue.setter
    def carValue(self, carValue):
        self.carValue = carValue
