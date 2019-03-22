n, m = [i for i in input().split()]
n = list(n)
m = int(m)
l = []
for i in range(1,m+1):
    l.append(n[-i])
l.reverse()
[print(i,end='') for i in l]