from datetime import datetime
expectedformat = '%Y-%m-%d %H:%M:%S'

dt = None
a = input('Enter date in YYYY-MM-DD HH:MM:SS format: \n')
try:
    dt = datetime.strptime(a, expectedformat)

except ValueError:
    print('Invalid datetime')

print(dt)

yeari = None
try:
    yeari = int(year)
except:
    pass
if year1 is not None:
    if yeari < 1900:
        print ("Year must be greater than 1900")
    elif yeari > 2020:
        print ("Year must be less than 2020"
    else:
        print ("Year not valid")
else:
    print ("Year "+year+" is invalid")