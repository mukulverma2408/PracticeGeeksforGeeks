#Python program to convert unix timestamp string to readable date
from datetime import datetime
epoch_time = 1294113662

dt = datetime.fromtimestamp(epoch_time)
print(dt, type(dt))