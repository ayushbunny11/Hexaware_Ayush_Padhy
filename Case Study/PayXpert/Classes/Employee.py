from datetime import datetime

class Employee:
    def __init__(self, employeeID, firstName, lastName, dateOfBirth, gender, email, phoneNum, address, position, joiningDate, terminationDate):
        self._employeeID = employeeID
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._gender = gender
        self._email = email
        self._phoneNum = phoneNum
        self._address = address
        self._position = position
        self._joiningDate = joiningDate
        self._terminationDate = terminationDate

    def calculateAge(self):
        current = datetime.now()
        curr_year = current.year

        dob = self._dateOfBirth
        dob_obj = datetime.strptime(dob, "%Y-%m-%d")
        dob_year = dob_obj.year

        return curr_year-dob_year - ((current.month, current.day)<(dob_obj.month,dob_obj.day))


