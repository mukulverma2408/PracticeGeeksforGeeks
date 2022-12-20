#Get Month from year and weekday
#Input : test_year = 1997, test_week = 27
#Output : 1997-07-07 00:00:00
#Explanation : 27th Week starts from 7 july in 1997

from datetime import date, datetime, timedelta
test_year = 2021
test_week = 27

dt1 = date(test_year, 1, 1)
print(dt1)
delta = timedelta(weeks=test_week)
dt2 = dt1+delta
print(dt2 - timedelta(dt2.weekday()))
