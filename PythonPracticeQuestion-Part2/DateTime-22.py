#Creating a list of range of dates in Python
from datetime import date,datetime, timedelta

test_date = date(1997, 1, 4)
K = 5
new_dt = []

for i in range(5):
    dt = (test_date + timedelta(days=i)).isoformat()
    new_dt.append(dt)

print(new_dt)
