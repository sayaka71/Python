# birth day of the week

# table
year_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
uruu_year_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
youbi = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
youbi_num = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}

# now
year_now = 2021
month_now = 6
day_now = 14
youbi_now = "Mon"

# birth
year_birth =1997
month_birth = 10
day_birth = 17

total_days = 0
for i in range(year_birth, year_now):
    if (i%4==0 and i%100!=0) or i%400==0:
        total_days += sum(uruu_year_day)
    else:
        total_days += sum(year_day)

# month_now
i = year_now
if (i%4==0 and i%100!=0) or i%400==0:
    total_days += sum(uruu_year_day[:month_now])
else:
    total_days += sum(year_day[:month_now])

# month_birth
i = year_birth
if (i%4==0 and i%100!=0) or i%400==0:
    total_days -= sum(uruu_year_day[:month_birth])
else:
    total_days -= sum(year_day[:month_birth])

total_days = total_days+day_now-day_birth

# youbi
a = total_days%7
print(youbi[(youbi_num[youbi_now]-a)%7-1])