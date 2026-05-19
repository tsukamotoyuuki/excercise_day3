def calc_sum_diff(func):
    def wrapper(*args, **kwargs):
        print("start func")

        result = func(*args, **kwargs)

        print("finish func")

        return result
    return wrapper


@calc_sum_diff
def funcAB_1(a, b):
    return a + b


def funcAB_2(a, b):
    return a - b


print(funcAB_1(10, 2))
print(funcAB_2(10, 2))

