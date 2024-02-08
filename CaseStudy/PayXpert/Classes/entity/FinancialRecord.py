from Employee import Employee


class FinancialRecord(Employee):
    def __init__(self, employeeID, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position,
                 joiningDate, terminationDate, recordID, recordDate, Description, amount, recordType):
        super().__init__(employeeID, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position,
                         joiningDate, terminationDate)
        self.recordID = recordID
        self.recordDate = recordDate
        self.Description = Description
        self.amount = amount
        self.recordType = recordType
