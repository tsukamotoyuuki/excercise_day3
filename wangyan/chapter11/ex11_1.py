with open("sample11_6_1.txt","r") as s,open("sample11_6_1_doubled.txt","w") as f:
    for line in s:
        num = int(line.strip())
        f.write(str(num * 2) + "\n")

with open("sample11_6_1_doubled.txt", "r") as f:
    print(f.read())



