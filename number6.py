#c русским не работает
with open('file.txt', 'r') as f:
    ls = {}
    for ln in f:
        h = ln.replace("-", " ").split()
        ls[h[0][:-1]] = sum([int(i) for i in h[1:]])
    print(ls)
