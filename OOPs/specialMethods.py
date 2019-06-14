class Employee:
    
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  ## self is the instance here
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

        Employee.number_of_employees += 1
    
    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay  = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


    def __str__(self):
        return "{} -> {}".format(self.fullName(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())



emp1 = Employee("Ashirwad", "Sangwan", 50000)
emp2 = Employee("Test","User", 70000)


print(len(emp1))
# print(repr(emp1))
# print(str(emp1))