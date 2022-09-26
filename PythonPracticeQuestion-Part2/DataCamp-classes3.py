class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def __str__(self):
        return ("Name : {0} \nSalary : {1}".format(self.name, self.salary))

class Manager(Employee):
    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project
    def __str__(self):
        return ("Name : {0} \nSalary : {1} \nProject : {2}".format(self.name, self.salary, self.project))

    def display(self):
        print("Manager ", self.name)

    def give_raise(self, amount, bonus=1.05):
        amount *=bonus
        Employee.give_raise(self, amount)

e1 = Employee("Mukul Verma", 50000)
print(e1)
m1 = Manager("Aman Pabby", 100000, "IM")
print(m1)
