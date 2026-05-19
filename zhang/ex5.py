scores = [55, 92, 38, 92, 75, 81]
l = sorted(scores)
nummax = 0
nummax2 = 0
if l[-1] > l[-2]:
    nummax = l[-1]
elif l[-1] == l[-2]:
    nummax2 = l[-3]

print(nummax, nummax2)
    

