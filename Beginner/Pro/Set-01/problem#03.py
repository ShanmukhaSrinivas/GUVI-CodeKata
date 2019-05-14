x, y = [i for i in input().split()]
k=[]
for i in range(min(len(x),len(y))):
    l = ord(y[i])-ord(x[i])
    if l > 0:
        k.append(l)
s = set(k)
