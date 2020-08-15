''' пример ввода:       funky_stYle
                        never gonna give you uup never gonna let u doown'''
def int_func(a):
    return a.capitalize()
print(int_func(input()))
print(*[int_func(i) for i in input().split()])