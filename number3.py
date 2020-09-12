a, b = ["winter", "spring", "summer", "eminem's diss AKA Fall"], {}
for ai, i in enumerate(a):
    b[ai] = str(i)
print(b[int(input())%12//3])