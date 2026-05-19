def greet(name, time=None):
    if time == "morning":
        print(f"{name}さん、おはようございます。")
    elif time == "noon":
        print(f"{name}さん、こんにちは。")
    elif time == "evening":
        print(f"{name}さん、こんばんは。")
    else:
        print(f"{name}さん、こんにちは。")  # time が None または不正な場合のデフォルト
