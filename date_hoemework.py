from datetime import datetime

print(datetime.now())

now = datetime.now()
print(now.year)

date = datetime(
    2026,
    12,
    31
)
print(date)

from datetime import datetime
from datetime import timedelta

future = datetime.now() + timedelta(days=30)
print(future)

date = datetime.strptime(
    "2027-01-01",
    "%Y-%m-%d"
)
print(date)