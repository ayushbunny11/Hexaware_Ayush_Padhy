from Employee import Employee

class Payroll(Employee):
    def __init__(self, payrollID, employeeID, payPeriodStartDate, payPeriodEndDate, basicSalary, overtimePay,
                 deductions, netSalary, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position,
                 joiningDate, terminationDate):
        super().__init__(employeeID, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position,
                         joiningDate, terminationDate)
        self._payrollID= payrollID
        self._employeeID = employeeID
        self._payPeriodStartDate = payPeriodStartDate
        self._payPeriodEndDate = payPeriodEndDate
        self._basicSalary = basicSalary
        self._overtimePay = overtimePay
        self._deductions = deductions
        self._netSalary = netSalary
