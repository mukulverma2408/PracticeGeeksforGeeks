#Write a Python program that takes a string of numbers and letters and return string which consists of letters.
def decode(str):
    newstr = ""
    num = ['1','2','3','4','5','6','7','8','9']
    for i in range(len(str)):
        if str[i] in num:
            char = str[i+1]
            newstr += int(str[i]) * char
    print(newstr)

decode("4A3B2C1D2A")
decode("4A3B2C1D3A")
decode("1P1H1P")
decode("4A3B3C1D2A1B1D4A1C")
