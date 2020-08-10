ch = str(input())
o = len(ch)
p = 0
while o:
    if int(ch[o - 1]) > p:
        p = int(ch[o - 1])
    o -= 1
print(p)
