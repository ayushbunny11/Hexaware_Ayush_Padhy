from Student import Student
from Course import Course


class Enrollment:
    def __init__(self, enrollmentID: int, student: Student, course: Course, enrollmentDate: str):
        self.student = student
        self.course = course
        self.enrollmentId = enrollmentID
        self.enrollmentDate = enrollmentDate

    def GetEnrollmentDetails(self):
        print("Enrollment Details: ")
        print(f"Enrollment ID: {self.enrollmentId}")
        print(f"Student ID: {self.student.studentID}")
        print(f"Course ID: {self.course.courseID}")
        print(f"Date: {self.enrollmentDate}")



# if __name__ == '__main__':
#     s1 = Student(1, "Ayush", "Bunny", "01-07-2001", "sddasd", "32434")
#     c1 = Course(2, "Science", 102, "Instructor 1")
#     e1 = Enrollment(1, s1, c1, "05-07-2023")
#
#     e1.GetEnrollmentDetails()
