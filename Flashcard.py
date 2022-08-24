class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '( ' + self.meaning + ')'
    flash = []
    print("Welcome to Flashcard APplication")
    while (True):
        word = input("Enter Word")
        meaning = input("Enter Meaning")
        flash.append((word, meaning))
        option = input("Enter 0, if you want to add another word")
        if (option):
            break

    print("Your Flashcard")
    for i in flash:
        print(i)