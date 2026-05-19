items = [0, 1, 0, 3, 12]
con = 0
for i in items:
    if i == 0:
        con += 1
        items.remove(0)
for i in range(con):
    items.append(0)

print(items)
