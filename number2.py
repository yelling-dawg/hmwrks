with open('file.txt', 'r') as f:
    lncntr,wrdcntr=0,0
    for ln in f:
        lncntr+=1
        wrdcntr+=len(ln.split())
    print("There is",lncntr,"lines and",wrdcntr,"words")