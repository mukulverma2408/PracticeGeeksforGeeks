#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class Methods:
    def getString(self):
        self.name = input("Whats your name : ")
        return self.name

    def printString(self):
        print("Welcome " + self.name.upper())

obj  = Methods()
obj.getString()
obj.printString()
