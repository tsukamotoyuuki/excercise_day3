import os
import shutil
os.makedirs("date",exist_ok=True)
with open("tmp.txt", "w"):
    pass

if os.path.exists("date/tmp.txt"):
    os.remove("date/tmp.txt")
shutil.move("tmp.txt","date/")
