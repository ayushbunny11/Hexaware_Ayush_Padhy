import re

from .IEmployeeService import IEmployeeService
from datetime import datetime
from simple_colors import *
from prettytable import PrettyTable


class EmployeeServiceImpl(IEmployeeService):

    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def GetEmployeeByID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        print(yellow("\nEmployee Information: "))
        print(blue("EmployeeID: "), result[0])
        print(blue("Employee Name: "), (result[1] + ' ' + result[2]))
        print(blue("DOB: "), str(result[3]))
        print(blue("Gender: "), result[4])
        print(blue("Email: "), result[5])
        print(blue("Phone Number: "), result[6])
        print(blue("Address: "), result[7])
        print(blue("Position: "), result[8])
        print(blue("Joining Date: "), result[9])
        if result[10] is not None:
            print(blue("Termination Date: "), result[10])
        else:
            print(blue("Termination Date: "), None)
        return result

    def GetAllEmployees(self):
        query = "Select * from employee"
        result = self.dbUtil.fetchAll(query)
        columns = ['ID', 'First Name', 'Last Name', 'DOB', 'Gender', 'Email', 'Phone', 'Address', 'Position',
                   'Joining Date', 'Termination Date']
        table = PrettyTable(columns)
        for res in result:
            table.add_row(res)
        print(table)

    def AddEmployee(self):
        print(yellow("\nEnter employee information: "))
        employee = {
            'empID': self.generateUniqueEmployeeID(),
            'firstName': input(blue("Enter your first name: ")),
            'lastName': input(blue("Enter your last name: ")),
            'dob': input(blue("Enter your DOB in (YYYY-MM-DD) format: ")),
            'gender': input(blue("Enter your gender(Male or Female): ")).capitalize(),
            'email': input(blue("Enter your EmailID: ")),
            'phone': input(blue("Enter your Phone Number: ")),
            'address': input(blue("Enter your Address: ")),
            'position': input(blue("Enter your position: ")),
            'joiningDate': datetime.now().strftime("%Y-%m-%d")
        }

        if not (self.checkEmailID(employee['email'])):
            raise Exception("EmailID exists!!!")
        if not (self.checkPhoneNumber(employee['phone'])):
            raise Exception("Phone Number exists!!!")

        if self.checkEmployeeDataValidation(employee):
            query = ("insert into employee(EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, "
                     "Address, Position, JoiningDate) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values = (
                employee['empID'], employee['firstName'], employee['lastName'], employee['dob'], employee['gender'],
                employee['email'].lower(), employee['phone'], employee['address'], employee['position'],
                employee['joiningDate'])
            self.dbUtil.executeQuery(query, values)
            print(green("SUCCESS: Employee Added!", 'bold'))
        else:
            raise Exception("InvalidDataFound")

    def UpdateEmployee(self):
        empID = int(input("Enter your Employee ID: "))

        if self.GetEmployeeByID(empID) is None:
            raise Exception("EmployeeNotFountException")

        while True:
            print("\nWhat do you want to update?")
            print("1. Email")
            print("2. Phone Number")
            print("3. Address")
            print("4. Position")
            print("5. Termination Date")
            print("6. Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                new_email = input("Enter your new emailID: ")
                if not self.validEmail(new_email):
                    raise Exception("InvalidEmailID")
                if not (self.checkEmailID(new_email)):
                    raise Exception("Email ID exists!!!")
                query = "update employee set Email=%s where EmployeeID = %s"
                value = (new_email.lower(), empID)
                self.dbUtil.executeQuery(query, value)
                print(blue("Email Updated to "), new_email)
            elif ch == 2:
                new_phone = input("Enter your new phone number: ")
                if not (self.checkEmailID(new_phone)):
                    raise Exception("Phone Number already exists!!!")
                query = "update employee set PhoneNumber=%s where EmployeeID = %s"
                value = (new_phone, empID)
                self.dbUtil.executeQuery(query, value)
                print(blue("Phone Number Updated to "), new_phone)
            elif ch == 3:
                new_address = input("Enter your new address: ")
                query = "update employee set Address=%s where EmployeeID = %s"
                value = (new_address, empID)
                self.dbUtil.executeQuery(query, value)
                print(blue("Address Updated to "), new_address)
            elif ch == 4:
                new_position = input("Enter your new position: ")
                query = "update employee set Position=%s where EmployeeID = %s"
                value = (new_position, empID)
                self.dbUtil.executeQuery(query, value)
                print(blue("Position Updated to "), new_position)
            elif ch == 5:
                terminationDate = input("Enter your termination date in (YYYY-MM-DD) format: ")
                query = "update employee set TerminationDate=%s where EmployeeID = %s"
                value = (terminationDate, empID)
                self.dbUtil.executeQuery(query, value)
                print(blue("Termination Date Updated to "), terminationDate)
            else:
                break

    def RemoveEmployee(self):
        empID = int(input("Enter Employee ID which you want to remove: "))
        if self.GetEmployeeByID(empID) is None:
            raise "EmployeeNotFoundException!!!"
        query = "delete from employee where EmployeeID = %s"
        value = (empID,)
        self.dbUtil.executeQuery(query, value)
        print(green("Success: ", 'bold'), red("Employee removed!", 'bold'))

    def get_no_of_employees(self):
        query = "select count(*) from employee"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueEmployeeID(self):
        empID = int(self.get_no_of_employees()) + 1
        while True:
            if self.CheckEmployeeID(empID) is None:
                return empID
            else:
                empID = empID + 1

    def checkEmailID(self, email):
        query = "select Email from employee"
        result = self.dbUtil.fetchAll(query)
        if email not in (res[0] for res in result):
            return True
        else:
            return False

    def checkPhoneNumber(self, phone):
        query = "select PhoneNumber from employee"
        result = self.dbUtil.fetchAll(query)
        if phone not in (res[0] for res in result):
            return True
        else:
            return False

    def validEmail(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, email):
            print(red("Invalid Email Entered!!!"))
            return False
        else:
            return True

    def checkEmployeeDataValidation(self, employee):
        if not employee['firstName'] or not employee['lastName'] or not employee['dob'] or not employee['gender'] or not \
                employee['email'] or not employee['phone'] or not employee['address'] or not employee['position']:
            print(red("Error: All fields must be filled."))
            return False

        try:
            datetime.strptime(employee['dob'], "%Y-%m-%d")
        except ValueError:
            print(red("Error: Invalid date format. Please use YYYY-MM-DD."))
            return False

        if not self.validEmail(employee['email']):
            return False

        if employee['gender'].lower() not in ['male', 'female']:
            print(red("Error: Gender must be either 'Male' or 'Female'."))
            return False

        return True

    def CheckEmployeeID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result
