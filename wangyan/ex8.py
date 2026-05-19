import random

number = 0
count = 0
n = 0
while n <1 :
    number = random.randint(1,6)
    count += 1
    if number != 1:

        continue
    else:
        break
print(count)