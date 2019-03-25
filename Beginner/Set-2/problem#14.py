#Find possible odds
n, m = [int(i) for i in input().split()]
for i in range(n,m):
    if (i%2)!=0:
        print(i)
