a = list(map(int, input().split()))
print(sum(a))
while (True):
    kha = input().split()
    try:
        khaha = kha.index('attack_helicopter')
        if khaha > 0:
            a.extend([int(it) for it in kha[:khaha]])
            print(sum(a))
        break
    except ValueError:
        a.extend([int(it) for it in kha])
        print(sum(a))
