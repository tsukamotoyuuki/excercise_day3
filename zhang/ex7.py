instances = ["db-server", "web-server-01", "cache", "load-balancer"]
arch = []
i = 0
len_instances = len(instances)
while len_instances == 0:
    i = len(instances[len_instances - 1])
    len_instances -= 1
    arch.append(i)

arch = sorted(arch)
print(arch[-1])

