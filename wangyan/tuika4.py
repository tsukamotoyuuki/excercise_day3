beforeChar = input("アルファベット1つを入力してください")
if beforeChar.islower() == True:
    change = beforeChar.upper()
else:
    change = beforeChar.lower()

print(change)