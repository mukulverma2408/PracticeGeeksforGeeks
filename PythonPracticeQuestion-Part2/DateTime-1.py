#Python program to print current year, month and day
from datetime import date
curr_date = date.today()
print("Current Year is {}, Current Month is {}, Current day is {}". format(curr_date.year, curr_date.month, curr_date.day))