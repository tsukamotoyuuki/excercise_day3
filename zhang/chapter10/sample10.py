# import re
# m = re.search("is", "This is test string")
# print(type(m))
# print(m)
#
# n = re.findall("is", "This is test string")
# print(type(n))
# print(n)
#
# print(re.search("AB*C", AC))
#
#
import re

num_of_games = 48
num_of_wins = 31
num = num_of_wins/num_of_games
s = "2016年12月2日"

print("Winning percentage: %.3f" %num)

print(f"Winning percentange: {num:.3f}")

print(re.search("(090|080)-\d{4}-\d{4}", "090-8888-9999"))
re.search("(\d{4})年(\d{2})")
print(re.findall(r"\d+", s))


