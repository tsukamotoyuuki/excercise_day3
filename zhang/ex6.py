items = [0, 1, 0, 3, 12]
index = 0
j = 0
for i in items:
    while index <= 5:
        if i[index] == 0:
            items.remove(0)
            index += 1
            j += 1
while j == 0:
    j -= 1
    i.append(0)
    
print(i)
        


