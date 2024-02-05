from datetime import datetime


class PaymentService:
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def addNewPaymentRecord(self):
        paymentID = self.generateUniquePaymentID()
        print("Fill up the Payment details: ")
        payments = {
            'paymentID': paymentID,
            'studentID': input("Enter the StudentID: "),
            'amount': float(input("Enter the amount: ")),
            'paymentDate': input("Enter the Payment Date in (YYYY-MM-DD) format: ")

        }
        query = "Insert into payments values(%s, %s, %s, %s)"
        values = (payments['paymentID'], payments['studentID'], payments['amount'], payments['paymentDate'])
        return self.dbUtil.executeQuery(query, values)

    def getPaymentDetails(self):
        studentID = input("Enter your studentID: ")
        query = "Select * from payments where studentID = %s"
        values = (studentID,)
        result = self.dbUtil.fetchall(query, values)
        return result

    def updatePaymentRecords(self):
        paymentID = input("Enter your paymentID: ")
        amount = input("Enter the amount")
        date = datetime.now().strftime("%Y-%m-%d")
        query = "Update payments set amount=%s, payment_date=%s where paymentID=%s"
        values = (amount, date, paymentID)
        return self.dbUtil.executeQuery(query, values)

    def get_no_of_payments(self):
        query = "Select count(*) from payments"
        result = self.dbUtil.fetchOne(query)
        return result[0]

    def generateUniquePaymentID(self):
        concat = ('PS', str(self.get_no_of_payments() + 1))
        return "".join(concat)
