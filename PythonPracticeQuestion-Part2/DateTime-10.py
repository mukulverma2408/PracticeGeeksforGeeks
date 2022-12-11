#Python – Divide date range to N equal duration
from datetime import datetime
test_date1 = datetime(1997, 1, 4)
test_date2 = datetime(1997, 1, 30)
N = 7
newlst = []
datediff = (test_date2 - test_date1)
#print(datediff)
#print(datediff/N)
New_Delta = (datediff/N)

while test_date2 >= test_date1:
    #print(test_date2, test_date1, New_Delta)
    test_date1 += New_Delta
    newlst.append(test_date1)

print(newlst)
