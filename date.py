from datetime import datetime

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)


from datetime import datetime
birthday = datetime(
    2000,
    5,
    10
)
print(birthday)

date = datetime(
    2025,
    1,
    31

)
print(date)


# to compare dates:
date1 = datetime(
    2025,
    1,
    1
)
date2 = datetime(
    2026,
    1,
    1
)
print(date2 > date1)

# to add days:

from datetime import timedelta
today = datetime.now()
tomorrow = today + timedelta(days=1)

# check token expiration
expire_date = datetime(
    2027,
    1,
    1
)
if datetime.now() < expire_date:
    print("Valid")


# transform a string to data

api_date = "2026-06-05"
date = datetime.strptime(
    api_date,
    "%Y-%m-%d"
)
print(date.year)