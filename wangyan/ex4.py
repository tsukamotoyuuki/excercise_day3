logs = ["INFO: boot", "ERROR: db connection", "WARN: high load", "ERROR: timeout"]
n = 0
for i in logs:
    if i[:5] == "ERROR":
        n +=1
print(n)
