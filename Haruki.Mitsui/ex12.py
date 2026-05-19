def greet(name: str, time: str):
    if time == "morning":
        print(name + "さん、おはようございます。")
    elif time == "noon":
        print(name + "さん、こんにちは。")
    elif time == "evening":
        print(name + "さん、こんばんは。")

greet("Mitsui","morning")