from IFinancialRecordService import IFinancialRecordService
from datetime import datetime


class FinancialRecordServiceImpl(IFinancialRecordService):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def AddFinancialRecord(self):

        record = {
            'RecordID': self.generateUniqueFRID(),
            'EmployeeID': input("Enter employeeID: "),
            'RecordDate': datetime.now().strftime("%Y-%m-%d"),
            'Description': input("Enter Description: "),
        }
        amount = float(input("Enter the amount"))
        recordType = input("Enter Record Type: Income or Expense: ")
        if recordType == "Income":
            amount = 1 * amount
        else:
            amount = -1 * amount
        query = "insert into financialrecord values(%s, %s, %s, %s, %s, %s)"
        values = (
            record['RecordID'], record['EmployeeID'], record['RecordDate'], record['Description'], amount, recordType)
        return self.dbUtil.executeQuery(query, values)

    def GetFinancialRecordById(self):
        recordID = int(input("Enter the recordID: "))
        query = "select * from financialrecord where RecordID = %s"
        values = (recordID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def GetFinancialRecordsForEmployee(self):
        employeeID = int(input("Enter the employeeID: "))
        query = "select * from financialrecord where RecordID = %s"
        values = (employeeID,)
        result = self.dbUtil.fetchAll(query, values)
        return result

    def GetFinancialRecordsForDate(self):
        recordDate = (input("Enter the Record Date in (YYYY-MM-DD) format: "))
        query = "select * from financialrecord where RecordDate = %s"
        values = (recordDate,)
        result = self.dbUtil.fetchAll(query, values)
        return result

    def get_no_of_records(self):
        query = "select count(*) from financialrecord"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueFRID(self):
        empID = int(self.get_no_of_records()) + 1
        return empID
