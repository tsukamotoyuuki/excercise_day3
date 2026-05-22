import csv
male = 0
female =0
with open(r"C:\Users\wangyan\Desktop\My python project\chapter11\sample11_2_1.csv","r") as c:
    reader = csv.DictReader(c)
    for line in reader:
        gender = line["gender"].strip()
        if gender == "M":
            male += 1
        elif gender == "F":
            female += 1
print(f"Male：{male},Female:{female}")