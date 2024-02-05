from DBUtil import DBUtil
from StudentInformationPortal import StudentInformationPortal
from PaymentService import PaymentService
from TeacherInformationPortal import TeacherInformationPortal
from EnrollmentReportGeneration import EnrollmentReportGeneration


class MainApp():
    def main(self):
        try:
            dbUtil = DBUtil(host='localhost', user='root', password='SQL@bunny11', port=3306, database='sisdb')
            sip = StudentInformationPortal(dbUtil)
            tip = TeacherInformationPortal(dbUtil)
            pService = PaymentService(dbUtil)
            erg = EnrollmentReportGeneration(dbUtil)
        except Exception as e:
            raise Exception(f"Error Connecting Server: {e}")

        while True:
            print("Welcome to the Portal!!!")
            print("Which portal do you want to open?")
            print("1. Student Portal")
            print("2. Teacher Portal")
            print("3. Admin Portal")
            print("4. Payment Portal")
            print("5. Exit Portal")
            ch = int(input("Enter: "))
            if ch == 1:
                while True:
                    print("Welcome to the Student Portal")
                    print("What do you want to do?")
                    print("1. Get All Students Information")
                    print("2. Register Yourself in the main database")
                    print("3. Register Yourself in a course")
                    print("4. Exit Student Portal")
                    sc = int(input("Enter: "))
                    if sc == 1:
                        print(sip.getStudentInformation())
                    elif sc == 2:
                        sip.addNewStudent()
                    elif sc == 3:
                        sip.enrollStudentInCourse()
                    else:
                        break
            elif ch == 2:
                while True:
                    print("Welcome to the Teacher Portal")
                    print("What do you want to do?")
                    print("1. Get All Teachers Information")
                    print("2. Register Yourself in the main database")
                    print("3. Register Yourself in a course")
                    print("4. Change a teacher assigned to a course")
                    print("5. Check Courses")
                    print("6. Exit Teacher Portal")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        print(tip.getTeacherInformation())
                    elif tc == 2:
                        tip.addNewTeacher()
                    elif tc == 3:
                        tip.assignCourseToTeacher()
                    elif tc == 4:
                        tip.changeTeacherAssignment()
                    elif tc == 5:
                        print(tip.getAllCourses())
                        print("True" if 'Computer Networks' in [course[0] for course in tip.getAllCourses()] else "False")
                    else:
                        break
            elif ch == 3:
                while True:
                    print("Welcome to the Admin Portal")
                    print("1. Get the Enrollment Report Information")
                    print("2. Exit Admin Portal")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        print(erg.generateReport())
                    else:
                        break
            elif ch == 4:
                while True:
                    print("Welcome to the Payment Service Portal")
                    print("What do you want to do?")
                    print("1. Get All Payments Information")
                    print("2. Add your payment information")
                    print("3. Update your Payment Record")
                    print("4. Exit Teacher Portal")
                    tc = int(input("Enter: "))
                    if tc == 1:
                        print(pService.getPaymentDetails())
                    elif tc == 2:
                        pService.addNewPaymentRecord()
                    elif tc == 3:
                        pService.updatePaymentRecords()
                    else:
                        break
            else:
                dbUtil.closeConnection()
                print("Thank You for using the portal!!!")
                break


if __name__ == '__main__':
    obj = MainApp()
    obj.main()
