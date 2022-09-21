#Write a Python program to find different ways where £2 be made using any number of coins.
#Having Problem understanding

#coins = [1, 2, 5, 10, 20, 50, 100, 200]
import re
str = '-100#^sd-300rfkj8902w3ir021@swf-20'

print(re.findall(r'-\d+', str))
print(re.findall(r'\d+', str))