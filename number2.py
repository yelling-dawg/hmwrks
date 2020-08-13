a=[input() for i in range(5)]
b=[input() for i in range(4)]
for i in range(0,(len(a)-len(a)%2),2):
    a[i],a[i+1]=a[i+1],a[i]
print(*a)
for i in range(0,(len(a)-len(a)%2),2):
    b[i],b[i+1]=b[i+1],b[i]
print(*b)