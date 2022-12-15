#Generate k random dates between two other dates
from datetime import date, timedelta
import random
test_date1 = date(2015, 6, 3)
test_date2 = date(2015, 7, 1)
K = 7

delta = ((test_date2 - test_date1).days)
day_to_add = []
dates = []
for i in range(1, 8):
    rand = random.randint(1, 28)
    dates.append(test_date1+timedelta(days=rand))


print(dates)