from datetime import datetime
from datetime import timezone
expectedformat = '%Y-%m-%d %H:%M:%S'

dt = None
yeari = None

a = input('Enter date in YYYY-MM-DD HH:MM:SS format:\n')
try:
    dt = datetime.strptime(a, expectedformat)

except ValueError:
    print('Invalid datetime')
    exit()

yeari = dt.year

if dt is not None:
    if yeari < 1900:
        print ("Year must be greater than 1900")
    elif yeari > 2020:
        print ("Year must be less than 2020")
    else:
        print ("Year is valid")
        print(dt)

timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
print(timestamp)