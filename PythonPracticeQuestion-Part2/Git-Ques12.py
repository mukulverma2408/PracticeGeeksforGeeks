#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

def calculateLetter(sentence):
    letter = 0
    digit = 0
    for i in sentence:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            letter +=1
        else:
            pass
    print("Letter are {0} and Digit are {1} ".format(letter, digit))

calculateLetter("Hello World! 123")




