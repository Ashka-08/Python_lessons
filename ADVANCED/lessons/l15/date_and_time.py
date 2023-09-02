# time, date, datetime

from datetime import time, date, datetime

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
                second=0, microsecond=24)
print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')
print('\n')
"""
d = datetime.date(2007, 6, 15)  -       2007-06-15
t = datetime.time(2, 14, 0, 24) -       02:14:00.000024
dt = datetime.datetime(2007, 6, 15, 2, 14, 0, 24)       -       2007-06-15 02:14:00.000024
"""

# Разница времени

from datetime import timedelta

delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5,
        milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')
# delta = datetime.timedelta(days=9, seconds=11045, microseconds=6007) -  9 days, 3:04:05.006007
print('\n')

# дельта может быть отрицательной

from datetime import timedelta

delta = timedelta(weeks=53, days=500, hours=73, minutes=101,
                seconds=303, milliseconds=67890,
                microseconds=1234567)
neg_delta = timedelta(days=-3, minutes=-42)
print(f'{delta = }\t-\t{delta}')
print(f'{neg_delta = }\t-\t{neg_delta}')
print('\n')
"""
delta = datetime.timedelta(days=874, seconds=10032, microseconds=124567)        -       874 days, 2:47:12.124567
neg_delta = datetime.timedelta(days=-4, seconds=83880)  -       -4 days, 23:18:00
"""


# Математика с датами

from datetime import datetime, timedelta

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')
print('\n')
"""
delta = datetime.timedelta(days=1702)   -       1702 days, 0:00:00
new_date = datetime.datetime(1536, 12, 13, 6, 0)        -       1536-12-13 06:00:00
"""


# Доступ к свойствам

from datetime import time, date, datetime, timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101,
                    seconds=303, milliseconds=60)
print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')
print('\n')
"""
6
0
2
374
"""


# метод replace для создания копии со значениями текущего объекта

from datetime import time, date, datetime, timedelta

t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)
print(f'{new_dt}\n{one_more_hour}')
print('\n')
"""
2012-06-15 02:14:00.000024
03:14:00.000024
"""


# методы работы с датой и временем

from datetime import datetime
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
print(dt) # 2007-06-15 02:14:00.000024
print(dt.timestamp()) # 1181855640.000024
print(dt.isoformat()) # 2007-06-15T02:14:00.000024
print(dt.weekday()) # 4
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))
# Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.
print('\n')

# обратные методы, позволяющие создать объекты datetime

from datetime import datetime

date_original = '2022-12-12 18:01:21.555470'
date_timestamp = 1181862840.000024
date_iso = '2007-06-15T02:14:00.000024'
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
original_date = datetime.fromisoformat(date_original)
timestamp_date = datetime.fromtimestamp(date_timestamp)
iso_date = datetime.fromisoformat(date_iso)
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(original_date) # 2022-12-12 18:01:21.555470
print(timestamp_date) # 2007-06-15 04:14:00.000024
print(iso_date) # 2007-06-15 02:14:00.000024
print(text_date) # 2007-06-15 02:14:00
print('\n')


# Задание

from datetime import datetime, timedelta

d = datetime.now()
td = timedelta(hours=1)
for i in range(24*7):
    if d.weekday() == 6:
        break
    else:
        d = d + td
    print(i, end=' ')
print('\n')
"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55
"""

# Фабричная функция namedtuple

from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(f'{type(User)}, {type(u_1)}')
"""
User(first_name='Исаак', last_name='Ньютон', birthday=datetime.datetime(1643, 1, 4, 0, 0))
<class 'type'>, <class '__main__.User'>
"""
print('\n')


# доступ к свойствам, используя точечную нотацию

from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(u_1.first_name, u_1.birthday.year)
"""
User(first_name='Исаак', last_name='Ньютон', birthday=datetime.datetime(1643, 1, 4, 0, 0))
Исаак 1643"""
print('\n')


# дефолтные значения

import time
from collections import namedtuple
from datetime import datetime
User = namedtuple('User', ['first_name', 'last_name', 'birthday'], 
                    defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
# time.sleep(3) # не сработает, т.к. datetime.now() создается 1 раз при запуске
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
"""
Иванов, 16:46:42
Галилео, 16:46:42
"""
print('\n')


# метод _replace создаст копию

from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b) # Point(x=6, y=3, z=0)
print('\n')

# Экземпляры можно сортировать

from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11), Point(2, 202, 1)]
print(sorted(data))
# [Point(x=2, y=3, z=4), Point(x=2, y=202, z=1), Point(x=3, y=7, z=11), Point(x=10, y=-100, z=-500)] 
print('\n')


# Как ключ для словаря

from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
    }
print(d)
mut_point = Point(2, [3, 4, 5], 6)
print(mut_point)
# d.update({mut_point: 'bad_point'}) # TypeError: unhashable type: 'list'
print('\n')
"""
{Point(x=2, y=3, z=4): 'first', Point(x=10, y=-100, z=-500): 'second', Point(x=3, y=7, z=11): 'last'}  
Point(x=2, y=[3, 4, 5], z=6)
"""