import time


def deco(func):
    def wrapper(*args, **kwargs):
        print(time.perf_counter())

        sss = func(*args, **kwargs)

        print(time.perf_counter())
        return sss
    return wrapper


@deco
def add(a, b):
    return a + b


print(add(100, 9999))
