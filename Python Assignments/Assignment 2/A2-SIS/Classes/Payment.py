from Student import Student

class Payment(Student):
    def __init__(self, paymentID:int, student:Student, amount:float, paymentDate:str):
        super().__init__(student.studentID, student.firstName, student.lastName, student.dob, student.email,
                         student.phone)
        self.paymentID = paymentID
        self.amount = amount
        self.paymentDate = paymentDate

    def getPaymentDetails(self):
        print("Payment Details:")
        print(f"Payment ID: {self.paymentID}")
        print(f"Student ID: {self.studentID}")
        print(f"Student Name: {self.firstName} {self.lastName}")
        print(f"Amount: {self.amount}")
        print(f"Date: {self.paymentDate}")


#
# if __name__ == '__main__':
#     s1 = Student(1, "Ayush", "Bunny", "01-07-2001", "sddasd", "32434")
#     p1 = Payment(1, s1, 500, "20-01-2024")
#
#     p1.getPaymenyDetails()