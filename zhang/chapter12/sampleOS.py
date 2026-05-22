# https://docs.python.jp/3/library/os.html
import os
# # すでに存在する場合はエラー
# os.mkdir('chapter12_mkdir_test')


# #
if not os.path.exists('chapter12_mkdir_test'):
    os.mkdir('chapter12_mkdir_test')



os.makedirs('chapter12_mkdir_test/test', exist_ok=True)
#
#
#
# 相対パスも指定可
# os.makedirs(r'../chapter12_mkdir_test/test', exist_ok=True)
#
# # 絶対パスも可
# os.makedirs(r'C:\Users\User\Desktop\test_mkdir', exist_ok=True)

#
print(os.listdir('.'))
#
# # 絶対パスも指定可
# print(os.listdir(r'C:\Users\winDH0044\Desktop'))


# 更新日時を取得
import datetime
print(datetime.datetime.fromtimestamp(os.path.getmtime("sampleOS.py")))