from ITaxService import ITaxService


class TaxServiceImpl(ITaxService):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def CalculateTax(self):
        employeeID = int(input("Enter EmployeeID: "))
        taxYear = int(input("Enter Tax Year: "))

        if self.GetEmployeeByID(employeeID) is None:
            raise Exception("EmployeeNotFoundException")

        query = "select sum(TaxAmount) from tax where EmployeeID = %s and TaxYear = %s group by EmployeeID, TaxYear"
        values = (employeeID, taxYear)
        result = self.dbUtil.fetchAll(query, values)
        return result

    def GetTaxById(self, taxID):
        query = "select EmployeeID, TaxAmount from tax where TaxID = %s"
        values = (taxID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def GetTaxesForEmployee(self, employeeID):
        query = "select EmployeeID, TaxAmount from tax where EmployeeID = %s"
        values = (employeeID,)
        result = self.dbUtil.fetchAll(query, values)
        return result

    def GetTaxesForYear(self, taxYear):
        query = "select TaxYear, TaxAmount from tax where TaxYear = %s"
        values = (taxYear,)
        result = self.dbUtil.fetchAll(query, values)
        return result

    def GetEmployeeByID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result[0]
