import random
a = 0
n = 0
while a != 1:
    a = random.randint(1,6)
    n += 1
    print(a)

print(f"振った回数{n}回")
