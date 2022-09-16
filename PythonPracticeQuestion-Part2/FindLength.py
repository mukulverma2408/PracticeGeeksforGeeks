#Write a Python program to find the length of the last word.
def FindLen(word):
    wordlist = word.split()
    return(len(wordlist[-1]))

print(FindLen("Python Exercises"))