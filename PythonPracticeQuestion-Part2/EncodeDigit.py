#Write a Python program that takes a string and encode it that the amount of symbols would be represented by integer and the symbol
#Having Issues with this one
def encoding(str):
    encoded = ""
    counter = 0
    for i in range(len(str)):
        if str[i-1] == str[i]:
            counter +=1
        else:
            encoded +=  str(counter) + str[i-1]
            counter = 0
    print(encoded)

encoding('AAAABBBCCDAAA')