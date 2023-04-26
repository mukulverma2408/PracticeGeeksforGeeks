#Write a program which accepts a sequence of words separated by whitespace as input to
# print the words composed of digits only.

import re

def FindDigit():
    sentence = input("Enter your sentence ")
    digit = re.findall("\d+", sentence)
    print(digit)

FindDigit()

