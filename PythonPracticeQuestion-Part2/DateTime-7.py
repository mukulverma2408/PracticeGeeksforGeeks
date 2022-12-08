#Convert “unknown format” strings to datetime objects in Python
from datetime import datetime
import dateutil.parser as parser
str1 = "19750503T080120"

dt_str = parser.parse(str1)
print(dt_str, type(dt_str))