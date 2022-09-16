#Progg to remove ith char from string

def RemoveChar(str, num):
    strlen = len(str)
    str1 = str[0:num]
    str2 = str[(num+1):(strlen+1)]
    print(str1+str2)

str = "Jaya is a bad boy"
RemoveChar(str, 3)