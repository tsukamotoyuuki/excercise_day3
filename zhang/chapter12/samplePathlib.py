from pathlib import Path

# 現在のディレクトリのPathオブジェクトを作成
current_dir = Path('.')

# パスの結合とファイルの存在確認
pathlib_file_path = current_dir / 'sampleDir3' / 'test.txt'
print(pathlib_file_path)
print(pathlib_file_path.is_file())


# import os
#
# # 現在のディレクトリのパスを取得
# current_dir = ""
#
# # パスの結合とファイルの存在確認
# os_path_file_path = os.path.join(current_dir, 'sampleDir3', 'test.txt')
# print(os_path_file_path)
# print(os.path.isfile(os_path_file_path))
