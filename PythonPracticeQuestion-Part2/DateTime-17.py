#Python Program to check date in date range
#Given a date list and date range, the task is to write a Python program to check whether any date exists in the list in a given range.
from datetime import datetime
test_list = [datetime(2019, 12, 30), datetime(2018, 4, 4), datetime(2016, 12, 21), datetime(2021, 2, 2), datetime(2020, 2, 3), datetime(2017, 1, 1)]
date_strt = datetime(2019, 3, 14)
date_end = datetime(2020, 1, 4)

for dt in test_list:
    if dt >= date_strt and dt <= date_end:
        print(True)
