import re

text1 = "error at: 2023-01-15 10:40"
dates = re.findall(r"\d{4}-\d{2}-\d{2}",text1)

print(dates)

text2 = "Error: File not found.\nwarning: Disk space low.\nerror: An unknown error occurred.Notice: System updated.\nNotice: System updated."
error = re.findall(r"^(?:error|warning):.*",text2,re.IGNORECASE | re.MULTILINE)
print(error)

text3 =  '<a href="http://example.com">test site </a>'
url = re.findall(r'(?:http://|https://)[\w.?=&]+', text3)
print(url)