#Python Program to Get total Business days between two dates
from datetime import date, datetime, timedelta

dt1 = date(2015, 6, 3)
dt2 = date(2015, 7, 1)
delta = (dt2 - dt1).days
dt = {}

for i in range (1, delta+1):
    newdt = (dt1+timedelta(i))
    #print(newdt, newdt.weekday())
    if (newdt.weekday()) < 5:
        dt[newdt] = 1
    else:
        dt[newdt] = 0
print(dt)
print("Total Business Days in between date range is : {}".format(sum(dt.values())))

