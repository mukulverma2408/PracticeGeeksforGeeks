#Isoformat to datetime – Python
#Converting isoformat to datetime

from datetime import datetime
dt = datetime.now()
print(dt, type(dt))

dt_iso = dt.isoformat()
print(dt_iso, type(dt_iso))

dt_dttyp = datetime.strptime(dt_iso, "%Y-%m-%dT%H:%M:%S.%f")
print(dt_dttyp, type(dt_dttyp))