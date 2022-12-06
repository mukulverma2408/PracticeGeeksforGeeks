#Convert string to datetime in Python with timezone
from datetime import datetime, tzinfo
str = "2022-12-06 22:03:03"
tm = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
print(tm)