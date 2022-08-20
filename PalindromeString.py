#Check the string is Palindrome
def CheckPalindrome(str):
    revstr = str[::-1]
    if (str == revstr):
        print("Palindrome, String is {}, Reverse String is {}".format(str, revstr))
    else:
        print("Not Palindrome, String is {}, Reverse String is {}".format(str, revstr))

str = "mukul"
CheckPalindrome(str)