#Find median from given data
m = int(input())
l = sorted([int(i) for i in input().split()])
if m%2 == 0:
    m = int(m/2)
    print(int((l[m]+l[m-1])/2))
else:
    m = int(m/2)
    print(l[m])
