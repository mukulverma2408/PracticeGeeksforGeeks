#Python code to display the dates from 2021 – Feb 1st to 2021 – March 1st
from datetime import date, datetime, timedelta
start_date = date(2021, 2, 1)
end_date = date(2021, 3, 1)
delta = timedelta(days=1)

while (start_date <= end_date):
    print(start_date)
    start_date += delta

