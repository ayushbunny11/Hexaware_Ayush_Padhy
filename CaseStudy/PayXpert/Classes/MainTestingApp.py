import unittest
import sys

sys.path.append(
    'F:\\Companies\\Hexaware\\Technical Foundation Training\\Python Training\\PyCharm '
    'learning\\PyCharm\\CaseStudy\\PayXpert\\Classes')

from util.DBUtil import DBUtil
from CollectionClass import CollectionClass
from dao.EmployeeServiceImpl import EmployeeServiceImpl
from dao.PayrollServiceImpl import PayrollServiceImpl

db_util = DBUtil(host='localhost', user='root', password='SQL@bunny11', port='3306', database='payxpert')
ccl = CollectionClass(db_util)
esl = EmployeeServiceImpl(db_util)
psl = PayrollServiceImpl(db_util)

gross = ccl.GrossSalaryCollection()
net = ccl.NetSalaryCollection()


class PayrollSystemTestCase(unittest.TestCase):
    def test_calculate_gross_salary_for_employee(self):
        query = "SELECT BasicSalary, OvertimePay FROM payroll"
        check = []
        for basic_salary, overtime_pay in db_util.fetchAll(query):
            check.append(int(basic_salary + overtime_pay))
        expected_gross_salary = check
        actual_gross_salary = gross
        self.assertEqual(actual_gross_salary, expected_gross_salary)

    def test_calculate_net_salary_after_deductions(self):
        query = "SELECT NetSalary, Deductions FROM payroll"
        netCheck = []
        for NetSalary, ded in db_util.fetchAll(query):
            netCheck.append(int(NetSalary + ded))
        expected_net_salary = netCheck
        actual_net_salary = net
        self.assertEqual(actual_net_salary, expected_net_salary)

    def test_verify_tax_calculation_for_high_income_employee(self):
        employeeID = 1
        taxYear = 2022
        expected_tax = 12000.00
        calculatedTax = float(psl.getTaxAmountForEmployee(employeeID, taxYear))
        self.assertEqual(calculatedTax, expected_tax)

    def test_process_payroll_for_multiple_employees(self):
        res = False
        employeeID, startDate, endDate = 1, '2020-05-01', '2021-07-15'
        if psl.GeneratePayroll(employeeID, startDate, endDate) is not None:
            res = True
        self.assertTrue(res, "Couldn't process payroll.")



    def test_verify_error_handling_for_invalid_employee_data(self):
        employee = {
            'empID': 1,
            'firstName': 'John',
            'lastName': 'Doe',
            'dob': '1980-05-15',
            'gender': 'Male',
            'email': 'fwadw@gmail.com',
            'phone': '12',
            'address': '123 Main St, London',
            'position': 'Manager',
            'joiningDate': '2020-01-01'
        }
        validation_result = esl.checkEmployeeDataValidation(employee)
        self.assertTrue(validation_result, "Invalid Data Found.")


if __name__ == '__main__':
    unittest.main()
