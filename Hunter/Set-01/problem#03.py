l = int(input())
z = []
k = [int(i) for i in input().split()]
for i in range(len(k)):
    if i == k[i]:
        z.append(str(i))
print(' '.join(z))
