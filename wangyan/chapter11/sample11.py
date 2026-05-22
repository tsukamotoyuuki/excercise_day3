import csv
import xml.etree.ElementTree as et
import json
with open("sample11_6_1.txt","w") as f:
    for i in range(1,11):
        f.write(str(i) +"\n")
        print(i)

sum =0
with open("sample11_6_1.txt","r") as s:
    for line in s:
        num = int(line.strip())
        sum += num
print(sum)

total = 0
count = 0
with open(r"C:\Users\wangyan\Desktop\My python project\chapter11\sample11_2_1.csv","r") as c:
    reader = csv.DictReader(c)
    for line in reader:
        total += int(line["age"])
        count += 1
print(f"{total/count:.1f}")

total1 = 0
count1 = 0
tree = et.parse(r"C:\Users\wangyan\Desktop\My python project\chapter11\sample11_3.xml")
root = tree.getroot()
for person in root:
    age = person.find("age").text
    total1 += int(age)
    count1 +=1

print(f"{total1/count1:.1f}")


with open(r"C:\Users\wangyan\Desktop\My python project\chapter11\sample11_4_1.json", "r") as f:
    data = json.load(f)

total2 = 0
count2 = 0

for person in data:
    total2 += person["age"]
    count2 += 1

print(f"{total2 / count2:.1f}")