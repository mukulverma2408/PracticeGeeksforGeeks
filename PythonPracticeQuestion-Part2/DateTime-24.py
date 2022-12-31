#Python program to Get Month Name from Month Number
#Input : test_date = datetime(2020, 4, 8)
#Output : April

from datetime import datetime, timedelta
test_date = datetime(2020, 4, 8)
print("Month Number is - {}".format(test_date.month))
mnth = datetime.strftime(test_date, '%B')
print("Month Name is - {}".format(mnth))


