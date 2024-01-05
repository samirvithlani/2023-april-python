#pass Date in params..

from datetime import date

month = 2
day =14
year= 2021


x = date(year, month, day)
print(x)

today = date.today()
print(today)


timeDiff = x - today
print(timeDiff)
days = timeDiff.days
months = int(days/30)
print(type(days))
print(months)
years = int(days/365)
print(years)

print("You are ",years," years ",months," months and ",days," days old")


