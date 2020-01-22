from datetime import datetime
expectedforamt = '%Y-%m-%d %H:%M:%S'
dt = None

a = input()
try:
    dt = datetime.strptime(a, expectedforamt)
except ValueError:
    print('Invalid datetime')
print(dt)