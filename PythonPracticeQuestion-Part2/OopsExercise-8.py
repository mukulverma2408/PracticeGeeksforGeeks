#Write a Python class to reverse a string word by word
class pysolution:
    def revstr(self, str):
        newlst = list(str.split())
        return(' '.join(newlst[::-1]))

print(pysolution().revstr('Mukul .py'))
