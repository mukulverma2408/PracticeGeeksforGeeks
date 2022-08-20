#Python Progg to reverse word in a string

def ReverseWord(str):
    MainStr = str.split(' ')
    #print(MainStr)
    #NewStr = MainStr[::-1]
    NewStr = reversed(MainStr)
    print(' '.join(NewStr))

str = "geeks quiz practice code"
ReverseWord(str)

