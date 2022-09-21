#Reverse each word of a string

def ReverseWord(str):
    newlst = []
    wordlst = str.split()
    for i in wordlst:
        new_word = i[::-1]
        newlst.append(new_word)
    print(' '.join(newlst))

ReverseWord('My name is mukul')