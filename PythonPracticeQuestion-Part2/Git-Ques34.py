#Please write a program which count and print the numbers of each character in a string input by console.

def countChar(sentence):
    dict = {}
    for i in sentence:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

sentence = input("Enter any String : ")
countChar(sentence)