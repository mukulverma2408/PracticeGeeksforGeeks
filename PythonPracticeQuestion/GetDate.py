# Python3 code to demonstrate working of
# Convert day number to date in particular year
# Using datetime.strptime()
from datetime import datetime
day_num=str(339)
year=str(2020)

print(datetime.strptime(year + day_num,"%Y%j"))