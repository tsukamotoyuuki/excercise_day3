import time

def deco(func):
    def wrapper(*args, **kwargs):
        s_time = time.perf_counter()
        func(*args, **kwargs)
        f_time = time.perf_counter()
        run_time = f_time - s_time
        print("実行時間:",run_time)
        return 0
    return wrapper

@deco
def loop():
    sum = 0
    for i in range(1,10001):
        for j in range(1,10001):
            sum += i*j

loop()
