from datetime import timezone, datetime
dt = datetime(2015, 10, 19, 4, 20, 'pm')
print(dt)
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
print(timestamp)

dt = datetime(2015, 10, 19)
print(dt)
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
print(timestamp)