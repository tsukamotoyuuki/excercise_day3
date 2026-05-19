ip = "192.168.1.999"
s1 = ip.split('.')
print(s1)
i = 0
a = 0
while i <= 4:
    a = int(s1[i])
    if 0 <= a <= 255:
        print("True")
    else:
        print("False")

    i += 1

