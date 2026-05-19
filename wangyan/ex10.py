ip = "192.168.1.999"
parts = ip.split(".")
Is_True = True
for p in parts:
    num = int(p)
    if 0 <= num <= 255:
        continue
    elif num <0 or num > 255:
        Is_True = False
        break
print(Is_True)
