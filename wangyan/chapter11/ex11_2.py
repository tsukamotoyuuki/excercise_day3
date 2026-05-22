sum = 0
with open("sample11_6_1.txt","r") as f:
    for line in f:
        if int(line) %2 == 0:
            sum += int(line)
print(sum)