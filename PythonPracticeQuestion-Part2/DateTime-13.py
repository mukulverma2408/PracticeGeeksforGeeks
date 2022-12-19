#How to convert Python’s .isoformat() string back into datetime object
from datetime import datetime

dt1 = datetime(2022, 12, 19, 22, 10, 50)
dt2 = dt1.isoformat()
print(dt1, type(dt1))
print(dt2, type(dt2))
dt3 = datetime.strptime(dt2, '%Y-%m-%dT%H:%M:%S')
print(dt3, type(dt3))