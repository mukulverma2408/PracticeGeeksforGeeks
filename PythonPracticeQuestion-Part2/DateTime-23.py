#Python – Find the closest date from a List
#Input : test_date_list = [datetime(2020, 4, 8), datetime(2016, 8, 18), datetime(2018, 9, 24), datetime(2019, 6, 10), datetime(2021, 8, 10)]
#test_date = datetime(2017, 6, 6)
#Output : 2016-08-18 00:00:00

from datetime import date, datetime, timedelta
test_date_list = [datetime(2020, 4, 8), datetime(2016, 8, 18), datetime(2018, 9, 24), datetime(2019, 6, 10), datetime(2021, 8, 10)]
test_date = datetime(2017, 6, 6)
dict = {}
for dt in test_date_list:
    delta = abs((test_date - dt).days)
    dict[dt] = delta
temp = min(dict.values())
print(dict)
print(temp)
for key, value in dict.items():
    if value == temp:
        print(key)