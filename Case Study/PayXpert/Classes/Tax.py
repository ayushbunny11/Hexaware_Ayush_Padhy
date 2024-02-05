from Employee import Employee


class Tax(Employee):
    def __init__(self, employeeID, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position,
                 joiningDate, terminationDate, taxID, taxYear, taxableIncome, taxAmount):
        super().__init__(employeeID, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position,
                         joiningDate, terminationDate)
        self.taxID = taxID
        self.taxYear = taxYear
        self.taxableIncome = taxableIncome
        self.taxAmount = taxAmount
