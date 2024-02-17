from datetime import datetime as dt
date1 = dt(2024,2,17,23,59,59)
date2 = dt(2024,2,18,23,59,59)
print(abs(date2 - date1).total_seconds())
