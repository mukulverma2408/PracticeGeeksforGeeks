#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

def sortWord(sentence):
    word = list(sentence.split(','))
    word.sort()
    print(','.join(word))

sortWord('without,hello,bag,world')
