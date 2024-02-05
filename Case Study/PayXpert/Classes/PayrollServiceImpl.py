from IPayrollService import IPayrollService


class PayrollServiceImpl(IPayrollService):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def GeneratePayroll(self, employeeID, startDate, endDate):
        if self.GetEmployeeByID(employeeID) is None:
            raise Exception("EmployeeNotFoundException")
        query = '''SELECT
                        e.EmployeeID,
                        e.FirstName,
                        e.LastName,
                        p.PayPeriodStartDate,
                        p.PayPeriodEndDate,
                        p.BasicSalary,
                        p.OvertimePay,
                        p.Deductions,
                        p.NetSalary
                    FROM
                        Employee e
                    INNER JOIN
                        Payroll p ON e.EmployeeID = p.EmployeeID
                    WHERE
                        e.EmployeeID = %s
                        AND p.PayPeriodStartDate >= %s
                        AND p.PayPeriodEndDate <= %s
                '''
        values = (employeeID, startDate, endDate)
        result = self.dbUtil.fetchAll(query, values)
        return result

    def GetPayrollById(self, payrollID):
        query = "SELECT * FROM payroll WHERE PayrollID=%s"
        values = (payrollID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def GetPayrollsForEmployee(self):
        employeeID = int(input("Enter the employeeID: "))
        query = "select * from payroll p join employee e on p.EmployeeID = e.EmployeeID where p.EmployeeID = %s"
        values = (employeeID,)
        return self.dbUtil.fetchAll(query, values)

    def GetPayrollsForPeriod(self):
        startDate = input("Enter the start date: ")
        endDate = input("Enter the end date: ")
        query = "select * from payroll p where p.PayPeriodStartDate >= %s and p.PayPeriodEndDate <= %s"
        values = (startDate, endDate)
        return self.dbUtil.fetchAll(query, values)

    def GetEmployeeByID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result[0]
