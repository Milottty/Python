import datetime

from babel.dates import format_date

current_datetime=datetime.datetime.now()
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)

current_date = datetime.datetime.now().date()

print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)

current_time = datetime.datetime.now().time()

print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)

specific_date = datetime.date(2024, 4, 2)
specific_time = datetime.time(12, 30, 9)

format_date = specific_date.strftime('%d-%m-%y')
print(format_date)