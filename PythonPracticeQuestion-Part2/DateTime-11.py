#Python – Last business day of every month in year
from datetime import datetime
import calendar
dt = datetime(2022, 12, 12, 13, 10, 10)
yr = dt.year

print(calendar.monthcalendar(yr,12))


