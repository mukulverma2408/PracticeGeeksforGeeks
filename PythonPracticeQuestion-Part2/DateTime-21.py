#Python – Extract date in String
#Input : test_str = "gfg at 2021-01-04"
#Output : 2021-01-04
#Explanation : Date format string found.
import re
from datetime import datetime, timedelta
test_str = "gfg at 2021-01-04"
str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
str2 = re.findall(r'\d{4}-\d{2}-\d{2}', test_str)
#print(str, type(str))
#print(str2, type(str2))

dt = datetime.strptime(str.group(), '%Y-%m-%d').date()
print(dt)