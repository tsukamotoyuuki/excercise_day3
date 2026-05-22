import csv
import xml.etree.ElementTree as et
import json

with open('Sample11_6_1.txt', "w") as f:
    for i in range(1,11):
        f.write(f'{i}\n')

with open('Sample11_6_1.txt', "r") as f:
    sum = 0
    for line in f:
        sum += int(line)
    print(sum)

with open(r'C:\Users\HARUKI MITSUI\MyPythonProject\chapter11\Sample11_2_1.csv', 'r', newline="") as f:
    reader = csv.reader(f)
    sum_age = 0
    p_count = 0
    for row in reader:
        sum_age += int(row[1])
        p_count += 1
    print(f'{sum_age / p_count:.1f}')


tree = et.parse(r'C:\Users\HARUKI MITSUI\MyPythonProject\chapter11\sample11_3.xml')
root = tree.getroot()
sum_age = 0
for person in root:
    age = person.find('age').text
    sum_age += int(age)
print(f'{sum_age / len(root):.1f}')


with open(r'C:\Users\HARUKI MITSUI\MyPythonProject\chapter11\sample11_4_1.json', "r") as f:
    people = json.load(f)
    sum_age = 0
    for person in people:
        sum_age += int(person['age'])
    print(f'{sum_age / len(people):.1f}')


