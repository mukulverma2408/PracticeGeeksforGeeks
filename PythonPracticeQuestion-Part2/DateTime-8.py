#Extract time from datetime in Python
from datetime import datetime
dt = datetime.now()
#tm = dt.strftime('%H:%M:%S')
#print(datetime.strptime(tm, '%H:%M:%S'))

print(dt.time())