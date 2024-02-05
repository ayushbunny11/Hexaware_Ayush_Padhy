class Customer:
    def __init__(self, customerID: int, firstName: str, lastName: str, email: str, phone: str, address: str):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address

    @property
    def customerID(self):
        return self.customerID

    @property
    def firstName(self):
        return self.firstName

    @property
    def lastName(self):
        return self.lastName

    @property
    def email(self):
        return self.email

    @property
    def phone(self):
        return self.phone

    @property
    def address(self):
        return self.address

    @customerID.setter
    def customerID(self, customerID):
        self.customerID = customerID

    @firstName.setter
    def firstName(self, firstName):
        self.firstName = firstName

    @lastName.setter
    def lastName(self, lastName):
        self.lastName = lastName

    @email.setter
    def email(self, email):
        self.email = email

    @phone.setter
    def phone(self, phone):
        self.phone = phone

    @address.setter
    def address(self, address):
        self.address = address

    def getCustomerDetails(self):
        print("Customer Details: ")
        print(f"ID: {self.customerID}")
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")


