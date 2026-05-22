import json
total2 =0
name =""
with open(r"C:\Users\wangyan\Desktop\My python project\chapter11\sample11_4_1.json", "r") as f:
    data = json.load(f)

    for person in data:
        age = person["age"]
        max_name = person["name"]
        if age >= total2:
            total2 = age
            name = max_name

print(f"{name},{total2}")
