from .ITaxService import ITaxService
from prettytable import PrettyTable


class TaxServiceImpl(ITaxService):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def showResultsTable(self, columns, result):
        table = PrettyTable(columns)
        print()
        for res in result:
            table.add_row(res)
        print(table)

    def calculateTaxOnIncome(self, empID, taxYear):
        query1 = ("select BasicSalary+OvertimePay-Deductions from payroll where EmployeeID=%s and Year("
                  "PayPeriodStartDate)= %s")
        values = (empID, taxYear)
        taxAmount = 0
        result = self.dbUtil.fetchOne(query1, values)
        if result is None:
            raise Exception("DataNotFound")
        taxableIncome = float(result[0])
        if 2020 <= taxYear <= 2022:
            if taxableIncome < 40000.00:
                taxAmount = 0
            elif 40000.00 < taxableIncome <= 75000.00:
                taxAmount = taxableIncome * 0.06
            elif 75000.00 < taxableIncome <= 100000.00:
                taxAmount = taxableIncome * 0.11
            elif 100000.00 < taxableIncome <= 150000.00:
                taxAmount = taxableIncome * 0.20
            else:
                taxAmount = taxableIncome * 0.30
        elif taxYear >= 2023:
            if taxableIncome < 42000.00:
                taxAmount = 0
            elif 42000.00 < taxableIncome <= 80000.00:
                taxAmount = taxableIncome * 0.07
            elif 80000.00 < taxableIncome <= 120000.00:
                taxAmount = taxableIncome * 0.14
            elif 120000.00 < taxableIncome <= 180000.00:
                taxAmount = taxableIncome * 0.24
            else:
                taxAmount = taxableIncome * 0.32

        return round(taxAmount, 2)

    def CalculateTax(self):
        employeeID = int(input("Enter EmployeeID: "))
        if self.GetEmployeeByID(employeeID) is None:
            raise Exception("EmployeeNotFoundException")

        taxYear = int(input("Enter Tax Year: "))
        self.AddTaxToDB(employeeID, taxYear)
        taxAmount = self.calculateTaxOnIncome(employeeID, taxYear)
        query = "Update tax set TaxAmount=%s where EmployeeID=%s and TaxYear=%s"
        values = (taxAmount, employeeID, taxYear)
        self.dbUtil.executeQuery(query, values)
        return f"Tax Amount for employeeID {employeeID} for {taxYear} is {taxAmount}"

    def updateNetSalary(self, empID, taxYear):
        query = "update payroll set NetSalary=%s where EmployeeID=%s and Year(PayPeriodStartDate)=%s"
        amount = float(self.getNetSal(empID, taxYear))
        taxAmount = float(self.calculateTaxOnIncome(empID, taxYear))
        salary = amount - taxAmount
        values = (salary, empID, taxYear)
        self.dbUtil.executeQuery(query, values)
        return True

    def GetTaxById(self, taxID):
        query = "select EmployeeID, TaxAmount from tax where TaxID = %s"
        values = (taxID,)
        result = self.dbUtil.fetchOne(query, values)
        if result is not None:
            return f"EmployeeID: {result[0]}\nTaxAmount: {result[1]}"
        else:
            raise Exception("TaxIDNotFound")

    def GetTaxesForEmployee(self, employeeID):
        query = "select EmployeeID, TaxYear, TaxAmount from tax where EmployeeID = %s"
        values = (employeeID,)
        result = self.dbUtil.fetchAll(query, values)
        columns = ['EmployeeID', 'TaxYear', 'TaxAmount']
        self.showResultsTable(columns, result)
        return result

    def GetTaxesForYear(self, taxYear):
        query = "select TaxYear, TaxAmount from tax where TaxYear = %s"
        values = (taxYear,)
        columns = ['TaxYear', 'TaxAmount']
        result = self.dbUtil.fetchAll(query, values)
        self.showResultsTable(columns, result)
        return result

    def GetEmployeeByID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def getNetSal(self, empID, taxYear):
        query1 = ("select BasicSalary+OvertimePay-Deductions from payroll where EmployeeID=%s and Year("
                  "PayPeriodStartDate)= %s")
        values = (empID, taxYear)
        result = self.dbUtil.fetchOne(query1, values)
        if result is None:
            raise Exception("NetSalaryNotFound")
        return result[0]

    def noOfTaxID(self):
        query = "select count(*) from tax"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueTaxID(self):
        empID = int(self.noOfTaxID()) + 1
        while True:
            if self.checkTaxID(empID) is None:
                return empID
            else:
                empID = empID + 1

    def checkTaxID(self, taxID):
        query = f"select * from tax where TaxID={taxID}"
        return self.dbUtil.fetchOne(query)

    def AddTaxToDB(self, empID, taxYear):
        query = "Insert into tax values(%s, %s, %s, %s, %s)"
        values = (self.generateUniqueTaxID(), empID, taxYear, self.getNetSal(empID, taxYear),
                  self.calculateTaxOnIncome(empID, taxYear))
        return self.dbUtil.executeQuery(query, values)
