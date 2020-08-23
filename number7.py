import json as js
with open('file.txt', 'r') as f:
    ls,lns={},0
    j={"average_profit":0}
    for ln in f:
        ln=ln.split()
        ad=int(ln[2])-int(ln[3])
        ls[ln[0]]=ad
        if ad>=0:
            j["average_profit"]+=ad
            continue
        lns+=1
    j["average_profit"]//=lns
jsls=js.dumps([j,ls])# я не совсем понимаю зачем это нужно