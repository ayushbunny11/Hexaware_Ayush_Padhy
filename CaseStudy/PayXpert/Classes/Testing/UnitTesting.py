import unittest
import sys

sys.path.append(
    '/PyCharm/CaseStudy/PayXpert/Classes')

from PyCharm.CaseStudy.PayXpert.Classes.util.DBUtil import DBUtil
from CollectionClass import CollectionClass
from PyCharm.CaseStudy.PayXpert.Classes.dao.EmployeeServiceImpl import EmployeeServiceImpl
from PyCharm.CaseStudy.PayXpert.Classes.dao.PayrollServiceImpl import PayrollServiceImpl
from PyCharm.CaseStudy.PayXpert.Classes.dao.TaxServiceImpl import  TaxServiceImpl
from unittest.mock import patch

db_util = DBUtil(host='localhost', user='root', password='SQL@bunny11', port='3306', database='payxpert')
ccl = CollectionClass(db_util)
esl = EmployeeServiceImpl(db_util)
psl = PayrollServiceImpl(db_util)
tsl = TaxServiceImpl(db_util)

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
        query = "SELECT NetSalary FROM payroll"
        netCheck = []
        for NetSalary in db_util.fetchAll(query):
            netCheck.append(float(NetSalary[0]))
        expected_net_salary = netCheck
        actual_net_salary = net
        self.assertEqual(actual_net_salary, expected_net_salary)

    def test_verify_tax_calculation_for_high_income_employee(self):
        employeeID = int(ccl.highIncomeEmployee()[0])
        taxYear = int(ccl.highIncomeEmployee()[2])
        expected_tax = float(ccl.highIncomeEmployee()[1])
        calculatedTax = float(tsl.calculateTaxOnIncome(employeeID, taxYear))
        self.assertEqual(calculatedTax, expected_tax)

    @patch('PayrollServiceImpl.PayrollServiceImpl.GeneratePayroll')
    def test_process_payroll_for_multiple_employees(self, mock_res):
        res = []
        employeeID = [1, 2, 3]
        mock_res.return_value = 'Mocked Result'
        for emp in employeeID:
            if mock_res(emp) == 'Mocked Result':
                res.append(True)
            else:
                res.append(False)
        self.assertTrue(all(res), "Couldn't process payroll.")

    def test_verify_error_handling_for_invalid_employee_data(self):
        employee = {
            'empID': 12,
            'firstName': 'John',
            'lastName': 'Doe',
            'dob': '1980-05-15',
            'gender': 'Male',
            'email': 'fwadw@gmail.com',
            'phone': '124124124',
            'address': '123 Main St, London',
            'position': 'Manager',
            'joiningDate': '2020-01-01'
        }
        validation_result = esl.checkEmployeeDataValidation(employee)
        self.assertTrue(validation_result, "Invalid Data Found.")


if __name__ == '__main__':
    unittest.main()
