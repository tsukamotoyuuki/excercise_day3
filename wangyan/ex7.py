instances = ["db-server", "web-server-01", "cache", "load-balancer"]
max = 0
for i in instances:
    if len(i) > max:
        max = len(i)
        str = i
print(str)