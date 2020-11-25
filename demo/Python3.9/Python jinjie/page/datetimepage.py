from datetime import datetime, timedelta, timezone

print(datetime.now())
print(type(datetime.now()))

dt = datetime(2020, 11, 18, 15, 31, 30)
print(dt)
print(dt.timestamp())
print(datetime.fromtimestamp(1605684690.0))
print(datetime.utcfromtimestamp(1605684690.0))
print(datetime.strptime("2020-11-18 15:36:11", "%Y-%m-%d %H:%M:%S"))
print(datetime.now().strftime('%a, %b %d %H:%M'))
print(datetime.now() + timedelta(hours=12))
print(datetime.now() - timedelta(days=1))
print(datetime.now() + timedelta(days=1, hours=2))

tz_utc_8 = timezone(timedelta(hours=8))

print(datetime.now().replace(tzinfo=tz_utc_8))

utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt1 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt1)

def to_timestamp(dt_str, tz_str):
    dt_1 = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    if tz_str.find('+') > -1:
        #return dt_1.timestamp()
        return dt_1.replace(tzinfo=timezone(timedelta(hours=int(tz_str[(tz_str.find('+')+1):tz_str.find(':')])))).timestamp()
    elif tz_str.find('-') > -1:
        #return dt_1.timestamp()
        return dt_1.replace(tzinfo=timezone(timedelta(hours=int(tz_str[tz_str.find('-'):tz_str.find(':')])))).timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t1, t2)
