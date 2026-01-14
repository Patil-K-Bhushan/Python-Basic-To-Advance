def sum(*args):
    # print(args)
    total = 0
    for item in args:
        total += item
    return total

print(sum(342, 2, 7))