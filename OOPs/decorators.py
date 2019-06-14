class Employee:
    
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last):  ## self is the instance here
        self.first = first
        self.last = last
        

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullName(self):
        return "{} {}".format.(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp1 = Employee("Ashirwad", "Sangwan")
emp2 = Employee("Test","User")



emp1.fullName = "Sheldon Cooper"
del emp1.fullName
print(emp1.email)
print(emp1.fullName)