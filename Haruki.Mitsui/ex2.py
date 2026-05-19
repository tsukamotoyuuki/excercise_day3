password = "secret1234"
sec_password = password[:2] + "*"*(len(password)-5) + password[-2:]
print(sec_password)
