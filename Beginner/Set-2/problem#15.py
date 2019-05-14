#Find possible evens
n, m = [int(i) for i in input().split()]
for i in range(n+1,m):
    if (i%2)==0:
        print(i)
