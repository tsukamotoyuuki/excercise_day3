password = "secret1234"
s = 0
while s < 10:
    if 1 < s < 8:
        print("*", end="")
    else:
        print(password[s], end="")
    s += 1
