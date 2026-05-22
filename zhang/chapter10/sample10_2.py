import re

text1 = "error at: 2023-01-15 10:40"
pattern1 = r"(\d{4}-\d{2}-\d{2})"
list1 = re.findall(pattern1, text1)
print(list)

text2 = "Error: File not found.\nwarning: Disk space low.\nerror: An unknown error occurred.Notice: System updated.\nNotice: System updated."
pattern2 = "^(?:error|warning):.*"
list2 = re.findall(pattern2, text2, re.MULTILINE|re.IGNORECASE)
print(list2[0])
print(list2[1])
print(list2[2])

text3 =  '<a href="http://example.com">test site </a>'
pattern3 = r"(?:https|http)://[^\"]+"
list3 = re.findall(pattern3, text3)
print(list3[0])