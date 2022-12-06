#Python program to print current year, month and day
from datetime import date, timedelta
#curr_date = date.today()
#print("Current Year is {}, Current Month is {}, Current day is {}". format(curr_date.year, curr_date.month, curr_date.day))

#Python get date from day number
def get_date(day_num, year):
    start_date = date(year, 1, 1)
    new_date = start_date + timedelta(int(day_num)-1)
    print("date on {} day of year {} is {}".format(day_num, year, new_date.strftime("%Y-%m-%d")))

get_date(339, 2020)
