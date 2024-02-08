

class CollectionClass:
    def __init__(self, dbUtil):
        self.conn = dbUtil

    def GrossSalaryCollection(self):
        query = "SELECT BasicSalary, OvertimePay FROM payroll"
        gross = []
        for basic_salary, overtime_pay in self.conn.fetchAll(query):
            gross.append(int(basic_salary+overtime_pay))

        return gross

    def NetSalaryCollection(self):
        query = "SELECT NetSalary, Deductions FROM payroll"
        netSal = []
        for NetSalary, ded in self.conn.fetchAll(query):
            netSal.append(int(NetSalary + ded))

        return netSal


