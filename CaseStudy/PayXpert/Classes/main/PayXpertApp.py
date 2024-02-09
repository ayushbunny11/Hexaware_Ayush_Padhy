from PyCharm.CaseStudy.PayXpert.Classes.dao.EmployeeServiceImpl import EmployeeServiceImpl
from PyCharm.CaseStudy.PayXpert.Classes.dao.PayrollServiceImpl import PayrollServiceImpl
from PyCharm.CaseStudy.PayXpert.Classes.dao.FinancialRecordServiceImpl import FinancialRecordServiceImpl
from PyCharm.CaseStudy.PayXpert.Classes.dao.TaxServiceImpl import TaxServiceImpl
from PyCharm.CaseStudy.PayXpert.Classes.util.DBUtil import DBUtil
from simple_colors import *


class PayXpertApp:
    def main(self):
        try:
            dbutil = DBUtil(host='localhost', user='root', password='SQL@bunny11', port='3306', database='payxpert')
        except Exception as e:
            raise Exception(f"Error Connecting Server: {e}")
        esl = EmployeeServiceImpl(dbutil)
        psl = PayrollServiceImpl(dbutil)
        frsl = FinancialRecordServiceImpl(dbutil)
        tsl = TaxServiceImpl(dbutil)

        print(yellow("\nWelcome to PayXpert! Your One Stop Payroll Manager.", "bold"))
        while True:
            print()
            print("Which service do you want to use?")
            print("1. Employee Service")
            print("2. Payroll Service")
            print("3. Tax Service")
            print("4. Financial Record Service")
            print("5. Exit App")
            ch = int(input("Enter: "))
            if ch == 1:
                print()
                print(yellow("Welcome to the Employee Service"))
                while True:
                    print("\nWhat do you want to do?")
                    print("1. Get All Employee Information")
                    print("2. Get Employee By ID")
                    print("3. Register Employee in the database")
                    print("4. Update Employee Information")
                    print("5. Remove Employee from Database")
                    print("6. Exit Employee Service")
                    sc = int(input("Enter: "))
                    if sc == 1:
                        esl.GetAllEmployees()
                    elif sc == 2:
                        empID = int(input("Enter employeeID: "))
                        esl.GetEmployeeByID(empID)
                    elif sc == 3:
                        esl.AddEmployee()
                    elif sc == 4:
                        esl.UpdateEmployee()
                    elif sc == 5:
                        esl.RemoveEmployee()
                    else:
                        break
            elif ch == 2:
                print()
                print(yellow("Welcome to the Payroll Service"))
                while True:
                    print("\nWhat do you want to do?")
                    print("1. Generate Payroll Information")
                    print("2. Get Payroll By ID")
                    print("3. Get Payrolls For Employee")
                    print("4. Get Payrolls For Period")
                    print("5. Exit Payroll Service")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        employeeID = int(input("Enter the employeeID: "))
                        res = psl.GeneratePayroll(employeeID)
                        if res is not None:
                            print(green(f"Successfully generated payroll for employeeID: {employeeID} with payrollID: {res}"))
                            print(red("Generated NET SALARY is without involving tax. To calculate net salary "
                                      "accurately, check tax services."))
                        else:
                            print(red("Error: Could Not generate Payroll!"))
                    elif tc == 2:
                        payrollID = int(input("Enter the payrollID: "))
                        psl.GetPayrollById(payrollID)
                    elif tc == 3:
                        psl.GetPayrollsForEmployee()
                    elif tc == 4:
                        psl.GetPayrollsForPeriod()
                    else:
                        break
            elif ch == 3:
                print()
                print(yellow("Welcome to the Tax Service"))
                while True:
                    print("\nWhat do you want to do?")
                    print("1. Calculate Total Tax")
                    print("2. Get Tax By Id")
                    print("3. Get Taxes For Employee")
                    print("4. Update Net Salary for Employee")
                    print("5. Get Taxes For Year")
                    print("6. Exit Payment Service")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        print(tsl.CalculateTax())
                    elif tc == 2:
                        taxID = int(input("Enter TaxID: "))
                        print(tsl.GetTaxById(taxID))
                    elif tc == 3:
                        employeeID = int(input("Enter the employeeID: "))
                        tsl.GetTaxesForEmployee(employeeID)
                    elif tc==4:
                        employeeID = int(input("Enter the employeeID: "))
                        taxYear = int(input("Enter the Tax Year: "))
                        if tsl.updateNetSalary(employeeID, taxYear):
                            print(green("Success: Update Net Salary Successfully!"))
                    elif tc == 5:
                        taxYear = int(input("Enter the Tax Year: "))
                        tsl.GetTaxesForYear(taxYear)
                    else:
                        break
            elif ch == 4:
                print()
                print(yellow("Welcome to the Financial Record Service"))
                while True:
                    print("\nWhat do you want to use?")
                    print("1. Add a Financial Record")
                    print("2. Get Financial Record By ID")
                    print("3. Get Financial Records For Employee")
                    print("4. Get Financial Records For Date")
                    print("5. Generate Financial Report")
                    print("6. Exit Service")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        frsl.AddFinancialRecord()
                        print("Successfully Added to the Database!")
                    elif tc == 2:
                        frsl.GetFinancialRecordById()
                    elif tc == 3:
                        frsl.GetFinancialRecordsForEmployee()
                    elif tc == 4:
                        frsl.GetFinancialRecordsForDate()
                    elif tc == 5:
                        frsl.FinancialReportGeneration()
                    else:
                        break
            else:
                dbutil.closeConnection()
                print("Thank You for using the Service!!!")
                break

if __name__ == '__main__':
    obj = PayXpertApp()
    obj.main()