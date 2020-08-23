with open('file.txt', 'w') as f:
    f.write(input()+"\n")
    f.write(input()+"\n")
    f.write(input()+"\n")
    f.write(input())
with open('file.txt', 'r') as f:
    wrdcntr,kool=0,0
    for ln in f:
        island=ln.split()
        if int(island[1])<20000:
            print(island[0])
        wrdcntr+=int(island[1])
        kool+=1
    print(wrdcntr//kool)