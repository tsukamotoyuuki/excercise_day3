import re
di = {}

with open('Sample.txt', "r", encoding="utf-8") as f:
    content = f.read()
    m = re.findall("(\w+)", content, re.MULTILINE | re.IGNORECASE)
    print(m)
    for i in m:
        if str(m) in di:
            di[m] += 1
        else:
            di[m] = 1

print(di)

# with open('Sample.txt', "r") as f:
