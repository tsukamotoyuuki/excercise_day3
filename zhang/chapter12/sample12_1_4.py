# import os
#
# def listup(path, depth=0):
#     # ディレクトリの中に入っていることがわかるようにインデントする
#     indent = '  ' * depth
#     print(indent + f'Now in {path}')
#
#     # ディレクトリ内のエントリ（ディレクトリ or ファイル）を処理
#     for entry in os.listdir(path):
#         # entryはベース名のみなのでjoinでパスにする
#         fullpath = os.path.join(path, entry)
#
#         if os.path.isdir(fullpath):
#             # ディレクトリの場合、自分自身を呼び出す
#             # 探索が深くなっていることがわかるようにdepthに1を足す
#             listup(fullpath, depth + 1)
#         else:
#             # ファイルの場合は表示のみ
#             print(indent + f'Found {fullpath}')
#
#     # ひとつのディレクトリの処理が終わったことがわかるように表示
#     print(indent + f'Leave {path}')
#
# listup('')



# from pathlib import Path
# p = Path('chapter12_test')
# p.mkdir()  # Pathが表す「chapter12」という名前のディレクトリを作成する


from pathlib import Path

def listup(path, depth=0):
    # ディレクトリの中に入っていることがわかるようにインデントする
    indent = '  ' * depth
    print(indent + f'Now in {path}')

    # os.listdir → Pathオブジェクトのiterdir
    # entryは「完全なパス」なので「パスを連結する」操作は不要
    for entry in path.iterdir():
        # オブジェクト自体に対して「ディレクトリですか？」と聞く
        if entry.is_dir():
            # ディレクトリの場合、自分自身を呼び出す
            # 探索が深くなっていることがわかるようにdepthに1を足す
            listup(entry, depth + 1)
        else:
            # ファイルの場合は表示のみ
            print(indent + f'Found {entry}')

    # ひとつのディレクトリの処理が終わったことがわかるように表示
    print(indent + f'Leave {path}')

# listupにはPathオブジェクトを渡すように変更
listup(Path('.'))