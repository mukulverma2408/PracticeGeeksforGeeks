#Python program to get the nth weekday after a given date
#Input : test_date = datetime.datetime(2017, 3, 14),
#Output : 2017-03-17

from datetime import date, datetime, timedelta
dt1 = date(2017, 3, 14)
weekday_idx = 4
dt1_weekday = dt1.weekday()

print(dt1, dt1_weekday)
delta = abs(dt1_weekday - weekday_idx)
print(dt1 + timedelta(delta))