from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fact():
    print(i)
    x += 1
    if x > 15:
        break