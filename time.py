from datetime import datetime
ts = int("78785999")
ts = int("78786000")
ts = int("94694400")


# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
from time import gmtime, strftime

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(ts)))

timestamp = datetime\
    .strptime('1972-12-31 23:59:59+0000', '%Y-%m-%d %H:%M:%S%z')\
    .timestamp()

print(timestamp)
399

import time
print(time.mktime(time.strptime('1972-06-30T23:59:60', "%Y-%m-%dT%H:%M:%S")))
print(time.mktime(time.strptime('1972-07-01T00:00:00', "%Y-%m-%dT%H:%M:%S")))

print(time.mktime(time.strptime('1972-07-30T23:59:60', "%Y-%m-%dT%H:%M:%S")))
print(time.mktime(time.strptime('1972-07-31T00:00:00', "%Y-%m-%dT%H:%M:%S")))
