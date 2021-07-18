class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  ## self is the instance here
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.number_of_employees += 1

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(
            self.pay * self.raise_amount
        )  ## we'll have to use this through instance or class variable

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def fromString(cls, emp_str):
        first, last, pay = emp_str.split("-")

        return cls(first, last, pay)


"""
You can also use instances instead of class in classmethods and it'll still work.
"""

emp1 = Employee("Ashirwad", "Sangwan", 50000)
emp2 = Employee("Test", "User", 70000)

print(Employee.raise_amount)
Employee.setRaiseAmount(1.05)
print(Employee.raise_amount)

str_emp1 = "Joe-Root-40000"

new_emp1 = Employee.fromString(str_emp1)
print(new_emp1.email)
