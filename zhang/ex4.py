logs = ["INFO: boot", "ERROR: db connection", "WARN: high load", "ERROR: timeout"] 
index = 0
i = 0
while logs[index] in logs:
    i += 1
    index += 1

print(i)
