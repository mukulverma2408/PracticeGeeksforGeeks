#Python – Find consecutive dates in a list of dates
#Input : [datetime(2019, 12, 30), datetime(2019, 12, 31), datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4)]
#Output : True

from datetime import datetime, timedelta
dt_lst = [datetime(2019, 12, 30), datetime(2019, 12, 31), datetime(2020, 1, 1), datetime(2020, 1, 3), datetime(2020, 1, 3), datetime(2020, 1, 4)]
for i in range(len(dt_lst)-1):
    delta = dt_lst[i+1] - dt_lst[i]
    op = True
    if (delta.days != 1):
        op = False
        break
print(op)
