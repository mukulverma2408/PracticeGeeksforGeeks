class Student:
    student_id = 10
    student_name = "Mukul"
    student_class = "Btech"

for key, value in Student.__dict__.items():
    print (key, value)