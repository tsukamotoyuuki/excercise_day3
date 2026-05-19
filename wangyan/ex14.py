import time

def deco(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("処理時間:", end - start, "秒")
        return result

    return wrapper

@deco
def add(a,b):
    return a+b
print(add(10,20))