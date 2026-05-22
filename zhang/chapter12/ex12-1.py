import os
import datetime
import shutil

now = datetime.datetime.now()
path = now.strftime("%Y%m%d")

def creat_dir():
    try:
        os.mkdir(path)
        print("creat success")
    except Exception as ex:
        print("creat fail")
        print(ex)

def creat_file():
    f = open("tmp.txt", "w")
    f.close()



creat_dir()
creat_file()
shutil.move("./tmp.txt", path)
