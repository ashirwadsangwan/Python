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
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        """
        We can inherit the __init__ method from the Employee class which is the
        parent class to Developer class.
        There are two methods one is by using super().__init__() and second one is
        by using Employee.__init__().
        """
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):

        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees == []
        else:
            self.employees = employees

    def addEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmployees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmp(self):
        for emp in self.employees:
            print("-->", emp.fullName())


dev1 = Developer("Ashirwad", "Sangwan", 50000, "Python")
dev2 = Developer("OmPrakash", "Shanmugam", 70000, "C++")

mgr1 = Manager("Sheldon", "Cooper", 100000, [dev1])
mgr1.addEmployee(dev2)
mgr1.removeEmployees(dev1)

print(mgr1.email)
mgr1.printEmp()
