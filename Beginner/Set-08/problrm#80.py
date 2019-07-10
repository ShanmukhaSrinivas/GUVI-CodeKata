n = k = list(input())
for i in n:
    print(i)
    if int(i) % 2 == 0:
        k.remove(i)
        print(k)
        print(n)
    else:
        continue
print(' '.join(k))
