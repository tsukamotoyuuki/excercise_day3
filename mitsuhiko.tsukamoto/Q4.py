logs = ["INFO: boot", "ERROR: db connection", "WARN: high load", "ERROR: timeout"]
c = 0
i = 0
while i < 3:
    if logs[i] in "ERROR":
        c += 1
    i += 1
print(c)
