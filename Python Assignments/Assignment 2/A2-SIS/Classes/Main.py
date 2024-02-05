from Course import Course
from Enrollment import Enrollment
from Payment import Payment
from Student import Student
from Teacher import Teacher

if __name__ == '__main__':
    s1 = Student(1, "Ayush", "Bunny", "01-07-2001", "ayush@11.com", "8456875621")
    c1 = Course(1, "Science", 201, "John Smith")
    t1 = Teacher(1, "John", "Smith", "js@11.com")
    e1 = Enrollment(1, s1, c1, "25-01-2024")
    p1 = Payment(1, s1, 5000, "30-01-2024")

    e1.GetEnrollmentDetails()
    p1.getPaymentDetails()
