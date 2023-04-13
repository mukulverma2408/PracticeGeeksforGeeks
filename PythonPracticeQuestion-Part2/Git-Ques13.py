#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

def CalculateCase(sentence):
    count = {"upper":0, "lower":0}
    for letter in sentence:
        if letter.upper():
            count["upper"]+=1
        elif letter.lower():
            count["lower"]+=1
    print(count)

CalculateCase("Hello World!")
