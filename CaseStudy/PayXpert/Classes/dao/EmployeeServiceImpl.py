from IEmployeeService import IEmployeeService
from datetime import datetime


class EmployeeServiceImpl(IEmployeeService):

    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def GetEmployeeByID(self, empID: int):
        query = "Select * from employee where EmployeeID = %s"
        values = (empID,)
        result = self.dbUtil.fetchOne(query, values)
        return result

    def GetAllEmployees(self):
        query = "Select * from employee"
        result = self.dbUtil.fetchAll(query)
        return result

    def AddEmployee(self):
        employee = {
            'empID': self.generateUniqueEmployeeID(),
            'firstName': input("Enter your first name:"),
            'lastName': input("Enter your last name:"),
            'dob': input("Enter your DOB in (YYYY-MM-DD) format: "),
            'gender': input("Enter your gender(Male or Female): "),
            'email': input("Enter your EmailID: "),
            'phone': input("Enter your Phone Number: "),
            'address': input("Enter your Address: "),
            'position': input("Enter your position: "),
            'joiningDate': datetime.now().strftime("%Y-%m-%d")
        }
        if not self.checkEmployeeDataValidation(employee):
            raise Exception("InvalidDataFound")

        if not (self.checkEmailID(employee['email'])):
            raise Exception("EmailID exists!!!")
        if not (self.checkPhoneNumber(employee['phone'])):
            raise Exception("Phone Number exists!!!")

        query = ("insert into employee(EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, "
                 "Address, Position, JoiningDate) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (employee['empID'], employee['firstName'], employee['lastName'], employee['dob'], employee['gender'],
                  employee['email'], employee['phone'], employee['address'], employee['position'],
                  employee['joiningDate'])
        self.dbUtil.executeQuery(query, values)
        print("Employee Added!!!")

    def UpdateEmployee(self):
        empID = int(input("Enter your Employee ID: "))

        if self.GetEmployeeByID(empID) is None:
            raise Exception("EmployeeNotFountException")

        while True:
            print("What do you want to update?")
            print("1. Email")
            print("2. Phone Number")
            print("3. Address")
            print("4. Position")
            print("5. Termination Date")
            print("6. Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                new_email = input("Enter your new emailID: ")
                if not (self.checkEmailID(new_email)):
                    raise Exception("Email ID exists!!!")
                query = "update employee set Email=%s where EmployeeID = %s"
                value = (new_email, empID)
                return self.dbUtil.executeQuery(query, value)
            elif ch == 2:
                new_phone = input("Enter your new phone number: ")
                if not (self.checkEmailID(new_phone)):
                    raise Exception("Phone Number already exists!!!")
                query = "update employee set PhoneNumber=%s where EmployeeID = %s"
                value = (new_phone, empID)
                return self.dbUtil.executeQuery(query, value)
            elif ch == 4:
                new_address = input("Enter your new address: ")
                query = "update employee set Address=%s where EmployeeID = %s"
                value = (new_address, empID)
                return self.dbUtil.executeQuery(query, value)
            elif ch == 5:
                new_position = input("Enter your new position: ")
                query = "update employee set Position=%s where EmployeeID = %s"
                value = (new_position, empID)
                return self.dbUtil.executeQuery(query, value)
            elif ch == 6:
                terminationDate = input("Enter your termination date: ")
                query = "update employee set TerminationDate=%s where EmployeeID = %s"
                value = (terminationDate, empID)
                return self.dbUtil.executeQuery(query, value)
            else:
                break

    def RemoveEmployee(self):
        empID = int(input("Enter Employee ID which you want to remove: "))
        query = "delete from employee where EmployeeID = %s"
        value = (empID,)
        self.dbUtil.executeQuery(query, value)
        print("Employee removed")

    def get_no_of_employees(self):
        query = "select count(*) from employee"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueEmployeeID(self):
        empID = int(self.get_no_of_employees()) + 1
        return empID

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

    def checkEmployeeDataValidation(self, employee):
        if self.GetEmployeeByID(employee['empID']) is None:
            return False

        if not employee['firstName'] or not employee['lastName'] or not employee['dob'] or not employee['gender'] or not employee['email'] or not employee['phone'] or not employee['address'] or not employee['position']:
            print("Error: All fields must be filled.")
            return False

        try:
            datetime.strptime(employee['dob'], "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            return False

        if employee['gender'].lower() not in ['male', 'female']:
            print("Error: Gender must be either 'Male' or 'Female'.")
            return False

        return True
