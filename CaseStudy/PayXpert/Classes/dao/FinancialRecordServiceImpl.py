from .IFinancialRecordService import IFinancialRecordService
from datetime import datetime
from simple_colors import *
from prettytable import PrettyTable


class FinancialRecordServiceImpl(IFinancialRecordService):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def showResultsTable(self, result):
        columns = ['RecordID', 'EmployeeID', 'RecordDate', 'Description', 'Amount', 'RecordType']
        table = PrettyTable(columns)
        print()
        for res in result:
            table.add_row(res)
        print(table)

    def AddFinancialRecord(self):

        record = {
            'RecordID': self.generateUniqueFRID(),
            'EmployeeID': int(input("Enter employeeID: ")),
            'RecordDate': datetime.now().strftime("%Y-%m-%d"),
            'Description': input("Enter Description: "),
        }
        if self.GetEmployeeByIDFromEmployee(record['EmployeeID']) is None:
            raise "EmployeeNotFoundException"

        amount = float(input("Enter the amount: "))
        recordType = input("Enter Record Type: Income or Expense: ")
        if recordType == "Income":
            amount = 1 * amount
        else:
            amount = -1 * amount
        query = "insert into financialrecord values(%s, %s, %s, %s, %s, %s)"
        values = (
            record['RecordID'], record['EmployeeID'], record['RecordDate'], record['Description'], amount, recordType)
        return self.dbUtil.executeQuery(query, values)

    def FinancialReportGeneration(self):
        query = '''select p.EmployeeID, p.PayPeriodStartDate, p.PayPeriodEndDate, BasicSalary, OvertimePay, 
        Deductions, t.TaxAmount, p.NetSalary from payroll p join tax t on p.EmployeeID = t.EmployeeID'''
        result = self.dbUtil.fetchAll(query)
        columns = ['EmployeeID', 'PayPeriodStartDate', 'PayPeriodEndDate', 'BasicSalary', 'OvertimePay', 'Deductions', 'TaxAmount', 'NetSalary']
        table = PrettyTable(columns)
        for res in result:
            table.add_row(res)
        print()
        print(yellow("Financial Report For all the Employees", 'italic'))
        print(table)

    def GetFinancialRecordById(self):
        recordID = int(input("Enter the recordID: "))
        query = "select * from financialrecord where RecordID = %s"
        values = (recordID,)
        result = self.dbUtil.fetchOne(query, values)
        if result is None:
            raise Exception("RecordNotFound")
        else:
            print(yellow("\nFinancial Record Information: "))
            print(blue("Record ID: "), result[0])
            print(blue("Employee ID: "), result[1])
            print(blue("Record Date: "), str(result[2]))
            print(blue("Description: "), result[3])
            print(blue("Amount: "), result[4])
            print(blue("Record Type: "), result[5])
            return result

    def GetFinancialRecordsForEmployee(self):
        employeeID = int(input("Enter the employeeID: "))
        if self.GetEmployeeByID(employeeID) is None:
            raise "EmployeeNotFoundException"
        query = "select * from financialrecord where EmployeeID = %s"
        values = (employeeID,)
        result = self.dbUtil.fetchAll(query, values)
        self.showResultsTable(result)
        return result

    def GetFinancialRecordsForDate(self):
        recordDate = (input("Enter the Record Date in (YYYY-MM-DD) format: "))
        query = "select * from financialrecord where RecordDate = %s"
        values = (recordDate,)
        result = self.dbUtil.fetchAll(query, values)
        self.showResultsTable(result)
        return result

    def get_no_of_records(self):
        query = "select count(*) from financialrecord"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueFRID(self):
        empID = int(self.get_no_of_records()) + 1
        return empID

    def GetEmployeeByID(self, empID: int):
        query = "Select * from financialrecord where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def GetEmployeeByIDFromEmployee(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result
