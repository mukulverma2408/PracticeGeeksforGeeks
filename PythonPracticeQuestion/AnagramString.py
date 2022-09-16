#Write a Python program to check if a given string is an anagram of another given string

def Anagram(str1, str2):
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    return (str1 == str2)
print(Anagram('anagram', 'nagaram'))
print(Anagram('cat', 'rat'))