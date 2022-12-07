#Python datetime to integer timestamp
from datetime import datetime

dt = datetime.now()
print(dt, type(dt))

epoch_time = int(dt.timestamp())
print(epoch_time, type(epoch_time))
