#Sort given data
m = int(input())
l = sorted([int(i) for i in input().split()])
for i in range(len(l)-1):
    print(l[i],end = " ")
print(l[len(l)-1])
