items = [0, 1, 0, 3, 12]
result = []
count = 0
for x in items:
    if x == 0:
        count += 1
    else:
        result.append(x)
for y in range(count):
    result.append(0)

print(result)