x = []
n = int(input())
for i in range(n):
    x.append(input())
k = x[0]
for i in x[1:]:
    l = []
    for j in range(min(len(k), len(i))):
        if k[j] == i[j]:
            l.append(k[j])
    k = ''.join(l)

print(k)
