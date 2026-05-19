instances = ["db-server", "web-server-01", "cache", "load-balancer"]
long = [""]
for i in instances:
    if len(i) > len(long[0]):
        long.clear()
        long.append(i)
    elif len(i) == len(long[0]):
        long.append(i)

print(long)
