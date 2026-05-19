def get_max(*args):
    if len(args) == 0:
        return 0
    max_value = args[0]
    for num in args[1:]:
        if num > max_value:
            max_value = num
    return max_value
