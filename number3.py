def my_func(x,y,z):
    t=[x,y,z]
    t.remove(min(t))
    return sum(t)
print(my_func(int(input()),int(input()),int(input())))