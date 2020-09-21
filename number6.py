import itertools as tit

a, b, ih = 1, [1, 1, 1, 1, 0, 1, 1, 1, 1], 1
for i in tit.cycle(b):
    print(i)
    if ih == 12:
        break
    ih += 1
for i in tit.count(100):
    print(i)
    if ih == 22:
        break
    ih += 1
