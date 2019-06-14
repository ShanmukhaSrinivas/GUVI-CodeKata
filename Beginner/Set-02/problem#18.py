a,b = [int(i) for i in input().split()]
l = []
for n in range(a,b):
    s = 0
    for i in str(n):
        s += int(i)**3
    if s == n:
        l.append(str(n))
p = (" ".join(i) for i in l)
print(p)
