from .IPayrollService import IPayrollService
from datetime import datetime
from dateutil.relativedelta import relativedelta
from simple_colors import *
from prettytable import PrettyTable


class PayrollServiceImpl(IPayrollService):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def GeneratePayroll(self, employeeID):
        if self.GetEmployeeByID(employeeID) is None:
            raise Exception("EmployeeNotFoundException")

        startDate = datetime.now().strftime('%Y-%m-%d')
        endDate = (datetime.now() + relativedelta(years=1)).strftime('%Y-%m-%d')

        positionQuery = f"select Position from employee where EmployeeID={employeeID}"
        res = self.dbUtil.fetchOne(positionQuery)[0]

        if res == 'Engineer':
            setBasicSalary = 95000.00
            setOvertimePay = 3000.00
            setDeductions = 6000.00
        elif res == 'Manager':
            setBasicSalary = 120000.00
            setOvertimePay = 6000.00
            setDeductions = 8000.00
        elif res == 'Specialist':
            setBasicSalary = 80000.00
            setOvertimePay = 1000.00
            setDeductions = 3000.00
        elif res == 'Analyst':
            setBasicSalary = 91200.00
            setOvertimePay = 3000.00
            setDeductions = 5500.00
        elif res == 'Supervisor':
            setBasicSalary = 135000.00
            setOvertimePay = 4500.00
            setDeductions = 10000.00
        elif res == 'Coordinator':
            setBasicSalary = 100000.00
            setOvertimePay = 2000.00
            setDeductions = 7500.00
        elif res == 'Technician':
            setBasicSalary = 60000.00
            setOvertimePay = 800.00
            setDeductions = 1000.00
        elif res == 'Director':
            setBasicSalary = 160000.00
            setOvertimePay = 8000.00
            setDeductions = 20000.00
        else:
            setBasicSalary = 200000.00
            setOvertimePay = 15000.00
            setDeductions = 32000.00

        setNetSalary = setBasicSalary+setOvertimePay-setDeductions

        query = '''Insert Into payroll
                    Values(%s, %s, %s, %s, %s, %s, %s, %s)
                '''
        values = (
            self.generateUniquePayrollID(), employeeID, startDate, endDate, setBasicSalary, setOvertimePay,
            setDeductions,
            setNetSalary)
        self.dbUtil.executeQuery(query, values)
        return values[0]

    def GetPayrollById(self, payrollID):
        query = "SELECT * FROM payroll WHERE PayrollID=%s"
        values = (payrollID,)
        result = self.dbUtil.fetchOne(query, values)
        if result is None:
            raise Exception("PayrollIDNotFoundException")
        else:
            print()
            print(yellow("\nPayroll Information: "))
            print(blue("Payroll ID: "), result[0])
            print(blue("Employee ID: "), result[1])
            print(blue("Pay Period Start Date: "), str(result[2]))
            print(blue("Pay Period End Date: "), str(result[3]))
            print(blue("Basic Salary: "), result[4])
            print(blue("Overtime Pay: "), result[5])
            print(blue("Deductions: "), result[6])
            print(blue("Net Salary: "), result[7])
            return result

    def GetPayrollsForEmployee(self):
        employeeID = int(input("Enter the employeeID: "))
        query = "select p.* from payroll p join employee e on p.EmployeeID = e.EmployeeID where p.EmployeeID = %s"
        values = (employeeID,)
        result = self.dbUtil.fetchAll(query, values)
        if not result:
            raise Exception("EmployeeNotFoundException")
        else:
            columns = ['PayrollID', 'EmployeeID', 'PayPeriodStartDate', 'PayPeriodEndDate', 'BasicSalary',
                       'OvertimePay', 'Deductions', 'NetSalary']
            table = PrettyTable(columns)
            for res in result:
                table.add_row(res)
            print(table)

    def GetPayrollsForPeriod(self):
        startDateStr = input("Enter the start date: ")
        endDateStr = input("Enter the end date: ")
        startDate = datetime.strptime(startDateStr, "%Y-%m-%d")
        endDate = datetime.strptime(endDateStr, "%Y-%m-%d")
        if startDate > endDate:
            raise Exception("InvalidDateInputException")
        query = "select * from payroll p where p.PayPeriodStartDate >= %s and p.PayPeriodEndDate <= %s"
        values = (startDate, endDate)
        result = self.dbUtil.fetchAll(query, values)
        if result is None:
            raise Exception("EmployeeNotFoundException")
        else:
            columns = ['PayrollID', 'EmployeeID', 'PayPeriodStartDate', 'PayPeriodEndDate', 'BasicSalary',
                       'OvertimePay', 'Deductions', 'NetSalary']
            table = PrettyTable(columns)
            for res in result:
                table.add_row(res)
            print(table)

    def GetEmployeeByID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def getTaxAmountForEmployee(self, employeeID, taxYear):
        query = "select TaxAmount from tax where EmployeeID=%s and TaxYear =%s"
        values = (employeeID, taxYear)
        result = self.dbUtil.fetchOne(query, values)
        if result is not None:
            return result[0]
        else:
            raise Exception("No data found!")

    def get_no_of_payrolls(self):
        query = "select count(*) from payroll"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniquePayrollID(self):
        payrollID = int(self.get_no_of_payrolls()) + 1
        return payrollID
