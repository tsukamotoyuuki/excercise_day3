import re

text1 = "error at: 2023-01-15 10:40"
print(re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", text1))

text2 = "Error: File not found.\nwarning: Disk space low.\nerror: An unknown error occurred.Notice: System updated.\nNotice: System updated."

r1 = re.findall("^(?:Error|Warning):.*", text2, re.MULTILINE | re.IGNORECASE)
print(r1)


text3 = '<a href="http://example.com">test site </a>'

print(re.search(r'(?:http|https)://[a-zA-Z0-9./?=&=]+', text3))


