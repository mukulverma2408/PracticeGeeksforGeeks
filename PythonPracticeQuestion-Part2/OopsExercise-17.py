#Student management system in Python
class Student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2

    def accept(self, name, rollno, marks1, marks2):
        ob = Student(name, rollno, marks1, marks2)
        ls.append(ob)

    def display(self, ob):
        print(ob.name, ob.rollno, ob.marks1, ob.marks2)

    def search(self, roll):
        for i in ls:
            if (ls[i].rollno == roll):
                return i

ls = []
obj = Student('', 0, 0, 0)
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
ch = int(input("Enter choice:"))
if(ch == 1):
    Student.accept(obj, 'A', 1, 90,  92)
