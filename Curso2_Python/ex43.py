#ex1
import calendar

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")

#ex2

from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

#ex5


import os

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())

# ex6
# Qual programa irá produzir o seguinte resultado:
# A:
import calendar
print(calendar.weekheader(2))
# B:
import calendar
print(calendar.weekheader())
# C:
import calendar
print(calendar.weekheader(3))
# D:
import calendar
print(calendar.week)

