# 辞書使う?
def greet(name, time):
    d = {"morning": "おはようございます。", "noon": "こんにちは。", "evening": "こんばんは"}
    print(name + "さん、" + d.get(time))


# greet("mitsuhiko", "noon")
