#Right-angled triangle formation
n = int(input())
for i in range(n,0,-1):
    l = []
    for _ in range(i,0,-1):
        l.append('1')
    print(' '.join(l))
