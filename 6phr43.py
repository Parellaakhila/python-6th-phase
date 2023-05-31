def sqrs(item):
    return item ** 2


lst = [i for i in range(1, 11)]
print(list(map(sqrs, lst)))
