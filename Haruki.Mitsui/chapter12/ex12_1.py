import os
import shutil

if not os.path.exists(f"data"):
    os.mkdir("data")

with open('tmp.txt', "w") as f:
    pass

shutil.move("tmp.txt", "data")
