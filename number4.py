with open('fill.txt', 'w') as fu:
    with open('file.txt', 'r') as f:
        kool = ["четыре", "три", "два", "один"]
        for ln in f:
            ln = ln.split()
            ln[0] = kool.pop()
            fu.write(" ".join(ln) + "\n")