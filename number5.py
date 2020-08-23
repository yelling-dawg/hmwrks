with open('file.txt', 'w') as f:
    f.write("100 896235803 17236419873408 1 434  6  455 3 56 35  34456 2 62 54 34352 353 6 75472 3231 679 173461029412")
with open('file.txt', 'r') as f:
    cntr=0
    for ln in f:
        o=[int(i) for i in ln.split()]
        cntr+=sum(o)
    print(cntr)