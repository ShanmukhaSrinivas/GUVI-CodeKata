m, n = [int(i) for i in input().split()]
x = [i for i in input().split()]
x = ''.join(x) 
for i in range(n):
    x = x[len(x)-1]+x[0:len(x)-1]
print(' '.join(x))
