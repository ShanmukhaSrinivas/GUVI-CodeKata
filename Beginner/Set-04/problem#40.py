n = int(input())
a = 0
b = 1
c = 0
k=[]
k.append(str(b))
for _ in range(1,n):
        c = a+b
        a = b
        b = c
        k.append(str(c))
print(' '.join(k))        