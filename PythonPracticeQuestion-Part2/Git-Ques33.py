#Define a class Person and its two child classes: Male and Female.
#All classes have a method "getGender"
#which can print "Male" for Male class and "Female" for Female class.

class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

amale = Male()
afemale = Female()

print(amale.getGender())
print(afemale.getGender())

