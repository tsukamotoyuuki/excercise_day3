import os
import datetime

now = datetime.datetime.now()
def creat_dir():
    try:
        path = now.strftime("%Y%m%d")
        os.mkdir(path)
        print("creat success")
    except Exception as ex:
        print("creat fail")
        print(ex)

creat_dir()


str = input(":")
print(type(str))
year, month, day = str.split("/")
y = int(year)
m = int(month)
d = int(day)
D = datetime.date(y, m, d)
print(f": {D.weekday()}　曜日")

DL = D + datetime.timedelta(weeks=2)
print(DL)


