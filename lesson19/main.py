# MM DD YY
# DD MM YY
# timestamp
from datetime import datetime, timedelta, tzinfo
from _pydatetime import _DAYNAMES, _MONTHNAMES
import time

class Adjusted_datetime(datetime):
    def ctime(self):
        weekday = self.toordinal() % 7 or 7
        return "%2d %s %s %02d:%02d:%02d %04d" % (
            self.day,
            _DAYNAMES[weekday],
            _MONTHNAMES[self.month],
            self.hour, self.minute, self.second,
            self.year)

current_time = time.localtime()
print(type(current_time))
print(current_time.tm_zone)

time_str = '2026-10-28 10:11:33'
date_format = '%Y-%m-%d %H:%M:%S'
t = time.strptime(time_str, date_format)
print(t)

# t = datetime(2026,10,28,10,11,33)
current_time = datetime.now()
# tzinfo
t = datetime.strptime(time_str, date_format)
print(t)
print(current_time)
print(current_time.tzinfo)
print(current_time.isoformat())
print(current_time.ctime())
print(current_time.strftime(date_format))

own_datetime = Adjusted_datetime.now()
print(own_datetime.ctime())
# timedelta
t_delta = current_time - t
print(t_delta)
print(type(t_delta))
future_date = own_datetime + timedelta(hours=340, minutes=333)
print(future_date)