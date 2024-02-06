class Customer:
    def __init__(self, customerID, cName, emailAddress, phoneNumber, Address, creditScore):
        self.customerID = customerID
        self.cName = cName
        self.email = emailAddress
        self.phone = phoneNumber
        self.address = Address
        self.creditScore = creditScore

    @property
    def CustomerID(self):
        return self.customerID

    @property
    def CName(self):
        return self.cName

    @property
    def Email(self):
        return self.email

    @property
    def PhoneNumber(self):
        return self.phone

    @property
    def Address(self):
        return self.address

    @property
    def creditScore(self):
        return self.creditScore

    @CustomerID.setter
    def CustomerID(self, customerID):
        self.customerID = customerID

    @CName.setter
    def CName(self, cName):
        self.cName = cName

    @Email.setter
    def Email(self, Email):
        self.email = Email

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self.phone = PhoneNumber

    @Address.setter
    def Address(self, Address):
        self.address = Address

    @creditScore.setter
    def creditScore(self, creditScore):
        self.creditScore = creditScore

