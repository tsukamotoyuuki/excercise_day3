password = 'secret1234'
middle = password[2:-2]
print(password[:2]+password[2:-2].replace(middle,'*'*len(middle))+password[-2:])