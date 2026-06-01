import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month 
day = now.weekday()

print(now,'\nyear:',year,'\nmonth:',month,'\nday:',day)

DOB = dt.datetime(year=2024,month=1,day=8)
print(DOB)
