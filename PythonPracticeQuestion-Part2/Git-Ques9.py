#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

def convertUpper():
    lst = []
    while True:
        sentence = input("Enter any sentence :- ")
        if sentence:
            lst.append(sentence)
        else:
            break
    for s in lst:
        print(s.upper())
    print(lst)

convertUpper()


