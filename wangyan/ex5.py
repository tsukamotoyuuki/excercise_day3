scores = [55, 92, 38, 92, 75, 81]
score_max = sorted(scores)
second = 0
max = 0
for s in score_max:
    if s >max:
        second = max
        max = s
    elif s < second and s != max:
        second = s
print(second)