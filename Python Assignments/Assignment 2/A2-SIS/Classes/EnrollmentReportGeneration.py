class EnrollmentReportGeneration:
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def generateReport(self):
        courseID = input("Enter the courseID: ")
        query = "select * from courses c join enrollments e on c.courseID = e.courseID where c.courseID = %s"
        value = (courseID,)
        return self.dbUtil.fetchall(query, value)