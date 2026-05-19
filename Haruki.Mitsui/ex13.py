def get_max(*args):
    count = 0
    max = 0
    if len(args) == 0:
        return count
    else:
        for i in args:
            if i > max:
                max = i
        return max


print(get_max(2,6,88,19,27))