

class CollectionClass:
    def __init__(self, dbUtil):
        self.conn = dbUtil

    def GrossSalaryCollection(self):
        query = "SELECT BasicSalary, OvertimePay FROM payroll"
        gross = []
        for basic_salary, overtime_pay in self.conn.fetchAll(query):
            gross.append(float(basic_salary+overtime_pay))

        return gross

    def NetSalaryCollection(self):
        query = "SELECT NetSalary FROM payroll"
        netSal = []
        for NetSalary in self.conn.fetchAll(query):
            netSal.append(float(NetSalary[0]))
        return netSal

    def highIncomeEmployee(self):
        query = ("select EmployeeID, TaxAmount, TaxYear from tax where EmployeeID = (select EmployeeID from payroll "
                 "order by BasicSalary desc limit 1)")
        return self.conn.fetchOne(query)



