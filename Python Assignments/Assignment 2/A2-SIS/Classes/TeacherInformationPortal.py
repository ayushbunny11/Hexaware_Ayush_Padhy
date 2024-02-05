class TeacherInformationPortal:
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def getTeacherInformation(self):
        query = "select * from teacher"
        result = self.dbUtil.fetchall(query)
        return result

    def addNewTeacher(self):
        teacherID = self.generateUniqueTeacherID()
        print("Fill up the Teacher details: ")
        teacher = {
            'teacherID': teacherID,
            'firstName': input("Enter the First Name: "),
            'lastName': input("Enter the Last Name: "),
            'email': input("Enter the emailID: "),
        }
        if not (self.checkEmailID(teacher['email'])):
            raise Exception("Email ID already exists")

        query = "Insert into teacher values(%s, %s, %s, %s)"
        values = (teacher['teacherID'], teacher['firstName'], teacher['lastName'], teacher['email'])
        return self.dbUtil.executeQuery(query, values)

    def assignCourseToTeacher(self):
        query = "Insert into courses values(%s, %s, %s, %s)"

        course_name = input("Enter the Course Name you have expertise in: : ")

        if course_name not in [course[0] for course in self.getAllCourses()]:
            course = {
                'courseID': self.generateUniqueCourseID(),
                'course_name': course_name,
                'credit': int(input("Enter the credits: ")),
                'teacherID': input("Enter the teacherID: ")
            }
            values = (course['courseID'], course['course_name'], course['credit'], course['teacherID'])
            return self.dbUtil.executeQuery(query, values)
        else:
            raise Exception("Course Already Exists!!!")

    def changeTeacherAssignment(self):
        query = "update courses set teacherID=%s where course_name = %s"
        teacherID = input("Enter the teacherID to be assigned: ")
        course_name = input("Enter the course name: ")
        values = (teacherID, course_name)
        return self.dbUtil.executeQuery(query, values)

    def get_no_of_teachers(self):
        query = "Select count(*) from teacher"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def get_no_of_courses(self):
        query = "Select count(*) from courses"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniqueTeacherID(self):
        concat = ('T0', str(self.get_no_of_teachers() + 1))
        return "".join(concat)

    def generateUniqueCourseID(self):
        concat = ('C0', str(self.get_no_of_courses() + 1))
        return "".join(concat)

    def checkEmailID(self, email):
        query = "select email from students"
        result = self.dbUtil.fetchall(query)
        if email not in result[0]:
            return True
        else:
            return False

    def getAllCourses(self):
        query = "select course_name from courses"
        result = self.dbUtil.fetchall(query)
        return result
