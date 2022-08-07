class Employee:
    def __init__(self, first, last, pay):  ## self is the instance here
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullName(self):
        return "{} {}".format(self.first, self.last)


emp1 = Employee("Ashirwad", "Sangwan", 50000)
emp2 = Employee("Test", "User", 70000)

print(emp1.email)
print(emp2.email)
print(emp1.fullName())
