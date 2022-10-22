#Python program to build flashcard using class in Python

class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return(self.word + '(' + self.meaning + ')' )

flash = []
print("Welcome to Flashcard Application")
while True:
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")

    flash.append(Flashcard(word, meaning))

    option = int(input("Press 1 if you want to exist else press 0 to add another flashcard "))

    if option:
        break
print("Printing your flashcard")
for i in flash:
    print(i)



