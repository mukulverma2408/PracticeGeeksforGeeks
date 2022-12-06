#How to add time onto a DateTime object in Python
from datetime import datetime, timedelta
dt_tm = datetime.today()
delta = timedelta(hours=1)
print("Original Time is {}".format(dt_tm))
print("Updated Time is {}".format(dt_tm+delta))