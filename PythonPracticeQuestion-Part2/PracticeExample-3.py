#Reverse a string in Python

def rev_str(str):
    newstr = ""
    for i in range(len(str)-1, -1, -1):
        print(str[i])
        newstr = newstr + str[i]
    print(newstr)

rev_str("Mukul")