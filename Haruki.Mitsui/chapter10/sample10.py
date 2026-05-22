import re

num_of_games = 48
num_of_wins = 31

print("Winning percentage: %.3f" % (num_of_wins/num_of_games))

print("Winning percentage: {0:.3f}".format(num_of_wins/num_of_games))
print(f"Winning percentage: {num_of_wins/num_of_games:.3f}")


call_num = "080-1234-5678"

print(re.search(r"^(080|090)-\d{4}-\d{4}", call_num))


r = re.compile(r"(\d{4}) 年 (\d{1,2}) 月 (\d{1,2}) 日")

date1 = '2016 年 12 月 2 日'
date2 = '2017 年 8 月 23 日'

d1 = r.search(date1)
d2 = r.search(date2)

print(d1.groups())
print(d2.groups())

