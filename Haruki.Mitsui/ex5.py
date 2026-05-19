scores = [55, 92, 38, 92, 75, 81]
max = 0
sec = 0
for i in scores:
    if i > max:
        sec = max
        max = i
    elif i > sec and i != max:
        sec = i

print(sec)
