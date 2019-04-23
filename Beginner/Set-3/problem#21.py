a = [int(i) for i in input().split()]
k=0
for i in range(1,a[0]+1):
    k+=a[1]+(i-1)*a[2]
print(k)
