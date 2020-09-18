from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "russian")

dt_now = datetime.now()
print(dt_now.strftime('%d.%m.%Y %H:%M'))
print(dt_now.strftime('%A %d %B %Y'))

dt2 = datetime(2020, 9, 17, 8, 3, 44)
delta = dt_now - dt2
yesterday = dt_now - delta
print(yesterday.strftime('%d.%m.%Y %H:%M'))

date_string = "01/01/25 12:10"
date_dt = datetime.strptime(date_string, '%d.%m.%Y %H:%M')
print(date_dt)