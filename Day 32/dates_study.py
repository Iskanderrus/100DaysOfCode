from datetime import datetime as dt

current_time = dt.now()
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.weekday())
current_time = current_time.strftime('%Y-%m-%d')
print(current_time)

birthday = dt(year=1980, month=8, day=30)
print(birthday)

