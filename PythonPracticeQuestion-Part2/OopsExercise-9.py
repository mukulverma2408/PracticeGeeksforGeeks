#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class pysolution:
    str = ''
    def get_String(self):
        self.str = input("Please Enter a String ")

    def print_String(self):
        print(self.str)

str1 = pysolution()
str1.get_String()
str1.print_String()