import time


def deco(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        print("time", finish - start)
        return result
    return wrapper


@deco
def add(a):
    i = 0
    for i in range(100000000):
        i += 1
    print(i)


add(1)

