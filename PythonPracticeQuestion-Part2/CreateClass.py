#Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

emp1 = Employee("Mukul", "ISS Trading Support", 50000)
print(emp1.name)
print(emp1.dept)
print(emp1.salary)
print(emp1.__dict__)