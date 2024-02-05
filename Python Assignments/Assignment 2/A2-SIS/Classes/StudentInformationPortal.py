from datetime import datetime


class StudentInformationPortal:
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def getStudentInformation(self):
        query = ("select studentID, concat(first_name,' ', last_name) as 'Name', date_of_birth, email, phone_number "
                 "from students")
        result = self.dbUtil.fetchall(query)
        return result

    def addNewStudent(self):
        studentID = self.generateUniqueStudentID()
        print("Fill up the student details: ")
        students = {
            'studentID': studentID,
            'firstName': input("Enter the First Name: "),
            'lastName': input("Enter the Last Name: "),
            'dob': input("Enter the date of birth: "),
            'email': input("Enter the emailID: "),
            'phone': input("Enter the phone Number:")
        }
        if not (self.checkEmailID(students['email'])):
            raise Exception("Email ID already exists")
        if not (self.checkPhoneNumber(students['phone'])):
            raise Exception("Phone Number already exists")

        query = "Insert into students values(%s, %s, %s, %s, %s, %s)"
        values = (students['studentID'], students['firstName'], students['lastName'], students['dob'], students['email'], students['phone'])
        return self.dbUtil.executeQuery(query, values)

    def enrollStudentInCourse(self):
        enrollmentID = self.generateUniqueEnrollmentID()
        enrollments = {
            'enrollmentID': enrollmentID,
            'studentID': input("Enter the studentID: "),
            'enrollment_date': datetime.now().strftime("%Y-%m-%d")
        }
        query = "Insert into enrollments values(%s, %s, %s, %s)"
        print("Choose which Course you want to enroll in: ")
        print("1. Introduction to Programming")
        print("2. Mathematics 101")
        print("3. Database Management")
        print("4. Web Development")
        print("5. Cyber Security")
        ch = int(input("Enter: "))
        if ch == 1:
            enrollments['courseID'] = 'C001'
            values = (enrollments['enrollmentID'], enrollments['studentID'], enrollments['courseID'],
                      enrollments['enrollment_date'])
            return self.dbUtil.executeQuery(query, values)
        elif ch == 2:
            enrollments['courseID'] = 'C011'
            values = (enrollments['enrollmentID'], enrollments['studentID'], enrollments['courseID'],
                      enrollments['enrollment_date'])
            return self.dbUtil.executeQuery(query, values)
        elif ch == 3:
            enrollments['courseID'] = 'C002'
            values = (enrollments['enrollmentID'], enrollments['studentID'], enrollments['courseID'],
                      enrollments['enrollment_date'])
            return self.dbUtil.executeQuery(query, values)
        elif ch == 4:
            enrollments['courseID'] = 'C004'
            values = (enrollments['enrollmentID'], enrollments['studentID'], enrollments['courseID'],
                      enrollments['enrollment_date'])
            return self.dbUtil.executeQuery(query, values)
        elif ch == 5:
            enrollments['courseID'] = 'C009'
            values = (enrollments['enrollmentID'], enrollments['studentID'], enrollments['courseID'],
                      enrollments['enrollment_date'])
            return self.dbUtil.executeQuery(query, values)

    def get_no_of_students(self):
        query = "Select count(*) from students"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def get_no_of_enrollments(self):
        query = "Select count(*) from enrollments"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueStudentID(self):
        concat = ('ST', str(self.get_no_of_students() + 1))
        return "".join(concat)

    def generateUniqueEnrollmentID(self):
        concat = ('EE', str(self.get_no_of_enrollments() + 1))
        return "".join(concat)

    def checkEmailID(self, email):
        query = "select email from students"
        result = self.dbUtil.fetchall(query)
        if email not in result[0]:
            return True
        else:
            return False

    def checkPhoneNumber(self, phone):
        query = "select phone_number from students"
        result = self.dbUtil.fetchall(query)
        if phone not in result[0]:
            return True
        else:
            return False
