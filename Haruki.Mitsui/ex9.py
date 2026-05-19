errors = ["404", "500", "404", "403", "500", "500"]
count = {}
for i in errors:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)
