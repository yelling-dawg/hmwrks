def my_func(x, y):
    ib = x
    for i in range(y - 1):
        ib *= x
    return ib


def my_cheatin_func(x, y):
    return x ** y


a, b = int(input()), int(input())
print(my_func(a, b))
print(my_cheatin_func(a, b))
