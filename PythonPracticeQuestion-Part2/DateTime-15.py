#Python – Get Most recent previous business day
#Input : test_date = datetime(2020, 1, 31)
#Output : 2020-01-30 00:00:00

from datetime import date, datetime, timedelta
dt1 = date(2022, 12, 18)
dayofweek = dt1.weekday()

if dayofweek == 0:
    delta = 3
elif dayofweek == 6:
    delta = 2
else:
    delta = 1

print("Input date is {}". format(dt1))
print("Day of week for Input Date is {}". format(dayofweek))
print("Previous Day is {}".format(dt1-timedelta(delta)))