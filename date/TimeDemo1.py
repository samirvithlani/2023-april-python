import time
from datetime import datetime

t = time.time()
print("Time in seconds since the epoch:", t)
t_ms = int(t*1000)
print("Time in milliseconds since the epoch:", t_ms)

date_time = datetime.fromtimestamp(t)
print("Date and Time:", date_time)


