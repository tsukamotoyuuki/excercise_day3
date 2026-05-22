import datetime
# from dateutil.relativedelta import relativedelta

# # 今日の日付を取得
today = datetime.date.today()
# print(type(today))
print(f'今日: {today}')
# #
# # # 特定の日付を作成
date = datetime.date(2025, 5, 20)
print(f'特定の日: {date}')
# #
# # # 日付の属性にアクセス 曜日=数値 月曜日~日曜日 =0~6
print(f'年: {date.year}, 月: {date.month}, 日: {date.day}, 曜日（だけメソッド）：{date.weekday()}')
#
print((today-date).days)


# # 5週間を表すことも可
datetimedelta = datetime.timedelta(days=5)
#
# # 5週間後
date = date + datetimedelta
print(f'5週間後: {date}')
#
# # 参考　1年と2ヶ月後の日時を計算
# one_month_later = today + relativedelta(months=2)
# print(f'1年と2か月後: {one_month_later}')
#
#
#
#
#
#
#
#
#
#
#
# # ex
# 2018年の8月14日が何曜日か「2018-08-14は○曜日」という形で表示してください
d = datetime.date(2018, 8, 14)
print(f"2018-08-14は: {d.weekday()}　曜日")
#
#
#
#
#
#
#
#
#
#
# # answer
# date = datetime.date(2018, 8, 14)
#
# # 曜日のリスト
# weekdays = ['月', '火', '水', '木', '金', '土', '日']
#
# # 曜日を取得して表示
# print(f'{date}は{weekdays[date.weekday()]}曜日')
# #
#
#
#
#
#
#
#
#
#
#
# #
now = datetime.datetime.now()
print(f'現在日時：{now}')
# #
# dt = datetime.datetime(2025, 5, 21, 22, 50, 5)
# print(f'特定の日時: {dt}')
# # #
# print(f'現在日時：{now.year}年{now.month}月{now.day}日　{now.hour}：{now.minute} {now.second}秒')
#
# # # 1日と10時間　20分　30秒　間
# diff = datetime.timedelta(days=1, hours=10, minutes=20, seconds=30)
# print(f'1日と10時間　20分　30秒　間後：{now+diff}')
#
# # 現在と特定の日時の間隔
# print(f'現在と特定の日時の間隔: {(now - dt).seconds}')
# print(f'現在と特定の日時の比較: {now > dt}')
#
#
# import locale
# now = datetime.datetime.now()
# locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
# print(now.strftime('ただいま、%Y年%m月%d日(%a)、%H時%M分です'))
# # #
# #
#
# input1 = "2024/1/1 10:20:20"
# # # #
# try:
#     dt1 = datetime.datetime.strptime(input1, '%Y/%m/%d %H:%M:%S')
# except:
#     dt1 = datetime.datetime(2020, 5, 21, 22, 50, 5)
#
# print(dt1)


# from dateutil import parser
#
# input2 = "2024/1 21 10:20:20"
# parsed_date = parser.parse(input2)
# print(parsed_date)





# ex 次のような形式で現在の日付と時刻を表示するプログラムを作成してください。
# ただいま、2024年05月21日(火)、15時30分です
import locale
now = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
print(now.strftime('ただいま、%Y年%m月%d日(%a)、%H時%M分です'))










# answer
# import locale
# import datetime
# locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

# 現在の日付と時刻を取得
# now = datetime.datetime.now()
#
# now_str = now.strftime('ただいま、%Y年%m月%d日(%a)、%H時%M分です')

# 結果を表示
# print(now_str)