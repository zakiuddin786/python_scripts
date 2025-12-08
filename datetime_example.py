from datetime import datetime, date, timedelta

now = datetime.now()

print(f"Current time is {now} and year is {now.year} month is {now.month} day is {now.day}")

date = date.today()
print(f"date is {date}")

# Formatted date
formatted_Date = now.strftime("%d / %m / %Y %H : %M")

print(f"formatted time is {formatted_Date}")

# date arithmetic

tomorrow = now + timedelta(days=1)

after_2_weeks = now + timedelta(days=14)

print(f"Tomorrow is {tomorrow} after 2 weeks it is {after_2_weeks}")