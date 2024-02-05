from EmployeeServiceImpl import EmployeeServiceImpl
from PayrollServiceImpl import PayrollServiceImpl
from FinancialRecordServiceImpl import FinancialRecordServiceImpl
from TaxServiceImpl import TaxServiceImpl
from DBUtil import DBUtil


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

        while True:
            print("Welcome to PayXpert!!!")
            print("Which service do you want to use?")
            print("1. Employee Service")
            print("2. Payroll Service")
            print("3. Financial Record Service")
            print("4. Tax Service")
            print("5. Exit App")
            ch = int(input("Enter: "))
            if ch == 1:
                while True:
                    print("Welcome to the Employee Service")
                    print("What do you want to do?")
                    print("1. Get All Employee Information")
                    print("2. Get Employee By ID")
                    print("3. Register Employee in the database")
                    print("4. Update Employee Information")
                    print("5. Remove Employee from Database")
                    print("6. Exit Employee Service")
                    sc = int(input("Enter: "))
                    if sc == 1:
                        print(esl.GetAllEmployees())
                    elif sc == 2:
                        empID = int(input("Enter employeeID: "))
                        print(esl.GetEmployeeByID(empID))
                    elif sc == 3:
                        esl.AddEmployee()
                    elif sc == 4:
                        esl.UpdateEmployee()
                    elif sc == 5:
                        esl.RemoveEmployee()
                    else:
                        break
            elif ch == 2:
                while True:
                    print("Welcome to the Payroll Service")
                    print("What do you want to do?")
                    print("1. Generate Payroll Information")
                    print("2. Get Payroll By ID")
                    print("3. Get Payrolls For Employee")
                    print("4. Get Payrolls For Period")
                    print("5. Exit Teacher Portal")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        employeeID = int(input("Enter the employeeID: "))
                        startDate = input("Enter the start date: ")
                        endDate = input("Enter the end date: ")
                        print(psl.GeneratePayroll(employeeID, startDate, endDate))
                    elif tc == 2:
                        payrollID = int(input("Enter the payrollID: "))
                        print(psl.GetPayrollById(payrollID))
                    elif tc == 3:
                        print(psl.GetPayrollsForEmployee())
                    elif tc == 4:
                        print(psl.GetPayrollsForPeriod())
                    else:
                        break
            elif ch == 3:
                while True:
                    print("Welcome to the Financial Record Service")
                    print("1. Add a Financial Record")
                    print("2. Get Financial Record By ID")
                    print("3. Get Financial Records For Employee")
                    print("4. Get Financial Records For Date")
                    print("5. Exit Service")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        frsl.AddFinancialRecord()
                    elif tc == 2:
                        print(frsl.GetFinancialRecordById())
                    elif tc == 3:
                        print(frsl.GetFinancialRecordsForEmployee())
                    elif tc == 4:
                        print(frsl.GetFinancialRecordsForDate())
                    else:
                        break
            elif ch == 4:
                while True:
                    print("Welcome to the Tax Service")
                    print("What do you want to do?")
                    print("1. Calculate Total Tax")
                    print("2. Get Tax By Id")
                    print("3. Get Taxes For Employee")
                    print("4. Get Taxes For Year")
                    print("5. Exit Payment Service")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        print(tsl.CalculateTax())
                    elif tc == 2:
                        taxID = int(input("Enter TaxID: "))
                        print(tsl.GetTaxById(taxID))
                    elif tc == 3:
                        employeeID = int(input("Enter the employeeID: "))
                        print(tsl.GetTaxesForEmployee(employeeID))
                    elif tc == 4:
                        taxYear = int(input("Enter the Tax Year: "))
                        print(tsl.GetTaxesForYear(taxYear))
                    else:
                        break
            else:
                dbutil.closeConnection()
                print("Thank You for using the portal!!!")
                break

if __name__ == '__main__':
    obj = PayXpertApp()
    obj.main()