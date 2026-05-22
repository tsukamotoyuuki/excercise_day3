import glob

# カレントディレクトリのすべてのテキストファイルを取得
# txt_files = glob.glob('*.py', recursive=True)
# print(txt_files)


# txt_filesItr = glob.iglob(r'**\*.txt', recursive=True)
# print(txt_filesItr)
# for txt_file in txt_filesItr:
#     print(txt_file)


# ex
# デスクトップ以下にある「*.txt」ファイルをサブディレクトリも含めて検索して一覧表示してください

# txt_files = glob.glob(r'C:\Users\User\Desktop\**\*.txt', recursive=True)
# print(txt_files)