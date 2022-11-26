class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name of the person is {}".format(self.name))
        print("Age of the person is {}".format(self.age))

class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        print("Name of the Student is {}".format(self.name))
        print("Age of the Student is {}".format(self.age))
        print("Section of the Student is {}".format(self.section))

student1 = Student('Mukul', 30, 'Computers')
student1.displayStudent()