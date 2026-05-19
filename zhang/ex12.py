def new_greet(func):
    def wrapper(*args, **kwargs):
        print("start func")

        sss = func(*args, **kwargs)

        print("finish func")
        return sss
    return wrapper


@new_greet
def greet(name, time):
    if time == "morning":
        return str(name + "さん" + "," + "おはようございます。")
    if time == "noon":
        return str(name + "さん" + "," + "こんにちは。")
    if time == "evening":
        return str(name + "さん" + "," + "こんばんは。")


print(greet(name="aaa", time="morning"))
print(greet(name="bbb", time="noon"))
print(greet(name="ccc", time="evening"))
