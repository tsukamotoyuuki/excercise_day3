ip = "192.168.1.999"
l = ip.split('.')
x = 0
for i in l:
    if 0 <= int(i) <= 255:
        continue
    else:
        x = 1

if x != 1:
    print("True")
else:
    print("False")
