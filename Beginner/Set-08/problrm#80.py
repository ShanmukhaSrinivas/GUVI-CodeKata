n = list(input())
for i in n:
    if int(i) % 2 == 0:
        n.remove(i)
print(' '.join(n))
