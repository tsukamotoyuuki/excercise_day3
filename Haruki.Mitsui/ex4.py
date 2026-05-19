logs = ["INFO: boot", "ERROR: db connection", "WARN: high load", "ERROR: timeout"]
con = 0
for i in logs:
    if i[:5] == 'ERROR':
        con += 1

print(con)
