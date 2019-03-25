#Find possible evens
n, m = [int(i) for i in input().split()]
if n%2 == 0:
    n += 1
for i in range(n,m):
    if (i%2)==0:
        print(i)
