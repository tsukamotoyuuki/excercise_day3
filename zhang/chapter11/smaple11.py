import xml.etree.ElementTree as et
import json

with open("sample11_6_1.txt", "w") as f:
    for i in range(1,11):
        f.write(str(i) + "\n")

# 2
sum = 0
with open("sample11_6_1.txt", "r") as f:
    for line in f:
        num = int(line.strip())
        sum += num

print(sum)

# 4
total1 = 0
count1 = 0
tree = et.parse("sample11_3.xml")
print(type(tree))
root = tree.getroot()
print(type(root))

for person in root:
    name = person.find("name").text
    print(name)
    gender = person.find("gender").text
    print(gender)
    age = int(person.find("age").text)
    print(age)
    total1 += age
    count1 += 1

print(f"平均年龄：{total1 / count1}")

# 5
total2 = 0
count2 = 0
with open("sample11_4_1.json", "r") as f:
    people = json.load(f)
    print(type(people))
    for person in people:
        age = int(person["age"])
        total2 += age
        count2 += 1

print(f"平均年龄：{total2 / count2}")
